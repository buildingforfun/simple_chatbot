# Simple Chatbot with Flask

This project demonstrates a basic chatbot application using Flask and ChatterBot. The chatbot is trained with a few simple responses and can be interacted with through a web interface.

## Requirements

- Python 3.x
- Flask
- ChatterBot

You can install the required libraries by running:

pip install Flask ChatterBot

## Project Structure

- `app.py`: The main Flask application file.
- `templates/`: A folder containing the HTML template for the chat interface.
  - `index.html`: The HTML file for the chat interface.

## How It Works

1. **Flask App**: The Flask app is defined in `app.py`. It creates a simple chatbot using ChatterBot and trains it with a few basic responses.
2. **Chat Interface**: The chat interface is defined in `index.html`. It includes a text input for the user to type messages, a send button, and a div to display the chat history.
3. **JavaScript**: The JavaScript code in `index.html` handles form submission, sends a POST request to the Flask app to get the chatbot's response, and updates the chat history.

## Key Features

- **Chatbot Training**: The chatbot is trained with a few basic responses using ChatterBot's `ListTrainer`.
- **Web Interface**: Users can interact with the chatbot through a simple web interface.
- **Dynamic Updates**: The chat history is updated dynamically as the user interacts with the chatbot.

## Running the App

1. Navigate to the project directory.
2. Run the Flask app using:

