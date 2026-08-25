"""
Text AI Chatbot 1.4

Text-Based Chatbot This text-based chatbot uses the ChatterBot library to provide intelligent and engaging responses. 
It is trained on custom dialogues and the ChatterBot corpus, enabling it to handle a wide range of conversational topics effectively.

Author: MGC https://github.com/mgc-00/ 
Updated: 07/02/2025, 25/08/2026

"""

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer


CUSTOM_CONVERSATION_1 = [
    "hi",
    "Hello there.",
    "what information can you give me?",
    "I can respond to general conversation and simple questions.",
    "what's your name?",
    "I'm a chatbot.",
    "how old are you?",
    "I'm ageless.",
    "how are you?",
    "I'm functioning well, thank you.",
    "what's your favorite food?",
    "I don't eat, but I can still talk about food.",
    "are you happy?",
    "I don't have emotions, but I'm here to help.",
    "i feel tired today",
    "You may want to get some rest.",
    "what's your job?",
    "My job is to respond to your questions."
]

CUSTOM_CONVERSATION_2 = [
    "hi",
    "Hi, how can I help?",
    "what's up?",
    "I'm here and ready to chat.",
    "how are you?",
    "I'm doing well, thanks.",
    "what's your name?",
    "I'm your text-based assistant.",
    "how old are you?",
    "I don't age like people do.",
    "what's your favorite food?",
    "I don't eat, so I don't have a favorite.",
    "are you happy?",
    "I don't experience emotions, but I can still have a conversation.",
    "i feel tired today",
    "Taking a break might help.",
    "what's your job?",
    "I answer questions and hold simple conversations."
]


def create_chatbot():
    return ChatBot(
        "TextBot",
        read_only=False,
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
                "maximum_similarity_threshold": 0.95,
            }
        ],
    )


def train_chatbot(bot):
    list_trainer = ListTrainer(bot)
    list_trainer.train(CUSTOM_CONVERSATION_1)
    list_trainer.train(CUSTOM_CONVERSATION_2)

    corpus_trainer = ChatterBotCorpusTrainer(bot)
    corpus_trainer.train("chatterbot.corpus.english")


def main():
    print("Training chatbot. This may take a moment...")

    bot = create_chatbot()
    train_chatbot(bot)

    print("TextBot is ready.")
    print("Type 'exit', 'quit', or 'bye' to end the chat.")

    while True:
        try:
            user_response = input("You: ").strip()

            if user_response.lower() in {"exit", "quit", "bye"}:
                print("TextBot: Goodbye!")
                break

            if not user_response:
                continue

            response = bot.get_response(user_response)
            print(f"TextBot: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nTextBot: Goodbye!")
            break


if __name__ == "__main__":
    main()
