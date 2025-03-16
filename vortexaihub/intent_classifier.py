import os
import numpy as np
import tensorflow as tf
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from vortexaihub.dataset import get_training_data


class IntentClassifier:
    def __init__(self, training_data=None, model_path='intent_model.h5', vectorizer_path='tfidf_vectorizer.pkl', encoder_path='label_encoder.pkl', train=False):
        """
        Initializes the IntentClassifier, either loading pretrained models or training a new one based on the 'train' flag.
        
        Args:
            training_data (list): Optional training data if retraining is needed.
            model_path (str): Path to save/load the Keras model.
            vectorizer_path (str): Path to save/load the TF-IDF vectorizer.
            encoder_path (str): Path to save/load the LabelEncoder.
            train (bool): If True, the model is trained; otherwise, the pretrained model is loaded.
        """
        
        self.model_path = model_path
        self.vectorizer_path = vectorizer_path
        self.encoder_path = encoder_path

        # Train or load models based on the train flag
        if train:
            self.train_model(training_data)
        else:
            self.load_model()
        
    def train_model(self, training_data=None):
            """Train the model with the provided training data."""
            print("Training the model...")

            if training_data is None:
                training_data = get_training_data()

            self.texts = [item["text"] for item in training_data]
            self.labels = [item["intent"] for item in training_data]

            # Encode the labels (intents)
            self.label_encoder = LabelEncoder()
            self.encoded_labels = self.label_encoder.fit_transform(self.labels)

            # Convert texts to TF-IDF features
            self.tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, 2))
            self.X = self.tfidf_vectorizer.fit_transform(self.texts).toarray()
            self.y = np.array(self.encoded_labels)

            # Train/test split
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

            # Build the model
            self.model = self._build_model()

            # Train the model
            self._train_model()

            # Save the trained model
            self.model.save(self.model_path)
            print(f"Model saved at {self.model_path}")

            # Save the TF-IDF vectorizer
            with open(self.vectorizer_path, 'wb') as file:
                pickle.dump(self.tfidf_vectorizer, file)
            print(f"TF-IDF Vectorizer saved at {self.vectorizer_path}")

            # Save the LabelEncoder
            with open(self.encoder_path, 'wb') as file:
                pickle.dump(self.label_encoder, file)
            print(f"LabelEncoder saved at {self.encoder_path}")

    def load_model(self):
            """Load the pretrained model, vectorizer, and encoder."""
            if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path) and os.path.exists(self.encoder_path):
                print("Loading pretrained model...")
                self.model = tf.keras.models.load_model(self.model_path)

                with open(self.vectorizer_path, 'rb') as file:
                    self.tfidf_vectorizer = pickle.load(file)

                with open(self.encoder_path, 'rb') as file:
                    self.label_encoder = pickle.load(file)
                print("Loaded pretrained model, vectorizer, and encoder.")
            else:
                print("Pretrained models not found. Please train the model first.")
                self.train_model()        

    def _build_model(self):
        """Build and compile the Keras model."""
        model = Sequential()
        
        # Input layer with 128 units (you can experiment with this)
        model.add(Dense(128, input_dim=self.X_train.shape[1], activation='relu'))
        
        # Dropout layer to prevent overfitting
        model.add(Dropout(0.5))
        
        # Hidden layer
        model.add(Dense(64, activation='relu'))
        
        # Output layer with softmax activation (for multi-class classification)
        model.add(Dense(len(np.unique(self.y)), activation='softmax'))
        
        # Compile the model
        model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        
        return model
    
    def _train_model(self):
        """Train the Keras model with the training data."""
        self.model.fit(self.X_train, self.y_train, epochs=20, batch_size=32, validation_data=(self.X_test, self.y_test))
    
    def predict_intent(self, query):
        """
        Predict the intent of a user query
        
        Args:
            query (str): The user's input query
            
        Returns:
            str: The predicted intent category
        """
        # Convert the query to the same features using the TF-IDF vectorizer
        query_tfidf = self.tfidf_vectorizer.transform([query]).toarray()
        
        # Make the prediction
        probs = self.model.predict(query_tfidf)
        
        # Get the index of the predicted class
        predicted_index = np.argmax(probs, axis=1)[0]
        
        # Decode the predicted index back to the intent label
        predicted_intent = self.label_encoder.inverse_transform([predicted_index])[0]
        
        return predicted_intent
