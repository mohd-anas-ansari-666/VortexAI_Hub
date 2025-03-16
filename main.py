import os
from vortexaihub.chatbot import ChatBot

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    """Display a welcome message"""
    clear_screen()
    print("=" * 50)
    print("           AI CHATBOT WITH INTENT CLASSIFICATION")
    print("=" * 50)
    print("Type 'exit' to quit, 'help' for assistance.\n")

def display_help():
    """Display help information"""
    print("\nYou can ask about:")
    print("  - Weather (e.g., 'What's the weather in Paris?')")
    print("  - Air Quality (e.g., 'How is the air quality in Beijing?')")
    print("  - News (e.g., 'Show me the latest technology news')")
    print("  - General questions (These will be answered by Gemini 1.5 Pro)")
    print("\nCommands:")
    print("  - exit: Exit the chatbot")
    print("  - help: Display this help information\n")

def main():
    """Main application entry point"""
    display_welcome()
    chatbot = ChatBot()
    
    print("Chatbot: " + chatbot.get_greeting())
    
    while True:
        try:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("\nChatbot: Goodbye! Have a great day!")
                break
                
            if user_input.lower() == "help":
                display_help()
                continue
            
            response = chatbot.process_query(user_input)
            print("\nChatbot:", response)
            
        except KeyboardInterrupt:
            print("\n\nChatbot: Session terminated by user. Goodbye!")
            break
        except Exception as e:
            print(f"\nChatbot: I'm sorry, something went wrong. Error: {str(e)}")

if __name__ == "__main__":
    main()