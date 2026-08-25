# Text Chatbot

## Overview
A simple command-line chatbot built in Python using the ChatterBot library. The project combines custom conversation examples with the ChatterBot English corpus to create a basic text-based conversational experience.

## Features
- Command-line chatbot interface
- Custom dialogue training data
- Additional training using the ChatterBot English corpus
- Simple interactive conversation loop
- Exit commands for ending the session cleanly

## Tech Stack
- Python
- ChatterBot
- ChatterBot Corpus
- spaCy

## Project Purpose
This project was built to explore rule- and corpus-based conversational systems in Python, with a focus on chatbot training workflows and simple natural language interaction.

## Requirements
- Python 3.x
- pip

## Installation
Install the required packages:

```bash
pip install chatterbot chatterbot-corpus spacy
python -m spacy download en_core_web_sm
How to Run
Run the chatbot from the project directory:

bash
python text_chatbot.py

Usage
Type a message and press Enter to chat
Type exit, quit, or bye to close the program

Notes
This project uses ChatterBot rather than a modern large language model. It is intended as a lightweight chatbot project demonstrating classic Python-based conversational AI tools.

Future Improvements
Expand custom training data
Improve response quality and consistency
Add conversation logging
Add a simple GUI version
