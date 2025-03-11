from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

# Create a chatbot
chatbot = ChatBot("MyChatBot")

# Train the chatbot with some basic responses
trainer = ListTrainer(chatbot)
trainer.train([
    "Hi", "Hello! How can I help you?",
    "How are you?", "I'm a bot, but thanks for asking!",
    "What's your purpose?", "I help answer questions!"
])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
