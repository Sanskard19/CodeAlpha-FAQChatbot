import json
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DATA_PATH = Path("data/faqs.json")


def load_faqs(path: Path = DATA_PATH):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


class FAQChatbot:
    def __init__(self, faqs):
        self.faqs = faqs
        self.questions = [faq["question"] for faq in faqs]
        self.answers = [faq["answer"] for faq in faqs]
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

    def get_best_match(self, user_question: str, top_k: int = 3):
        user_vector = self.vectorizer.transform([user_question])
        similarities = cosine_similarity(user_vector, self.question_vectors).flatten()
        ranked_indices = similarities.argsort()[::-1]

        best_index = ranked_indices[0]
        related = []
        for index in ranked_indices[1:top_k]:
            related.append(
                {
                    "question": self.questions[index],
                    "score": float(similarities[index]),
                }
            )

        return {
            "best_question": self.questions[best_index],
            "answer": self.answers[best_index],
            "score": float(similarities[best_index]),
            "related": related,
        }


def build_chatbot():
    return FAQChatbot(load_faqs())


if __name__ == "__main__":
    bot = build_chatbot()
    while True:
        query = input("Ask a question (or type quit): ").strip()
        if query.lower() == "quit":
            break
        result = bot.get_best_match(query)
        print("\nBest Match:", result["best_question"])
        print("Answer:", result["answer"])
        print("Confidence:", round(result["score"], 4))
        print()
