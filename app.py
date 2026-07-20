from flask import Flask, jsonify, render_template, request

from chatbot import build_chatbot

app = Flask(__name__)
chatbot = build_chatbot()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/ask", methods=["POST"])
def ask():
    payload = request.get_json(force=True)
    user_question = payload.get("question", "").strip()

    if not user_question:
        return jsonify({"error": "Question is required."}), 400

    result = chatbot.get_best_match(user_question)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
