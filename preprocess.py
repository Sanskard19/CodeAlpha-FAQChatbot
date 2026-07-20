import json
import re
from pathlib import Path

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
except ImportError as exc:
    raise SystemExit("Install requirements first: pip install -r requirements.txt") from exc

DATA_PATH = Path("data/faqs.json")
OUTPUT_PATH = Path("data/processed_faqs.json")


def ensure_nltk():
    for pkg in ["punkt", "stopwords"]:
        try:
            nltk.data.find(f"tokenizers/{pkg}" if pkg == "punkt" else f"corpora/{pkg}")
        except LookupError:
            nltk.download(pkg)


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def preprocess_text(text: str, stop_words: set[str]) -> list[str]:
    cleaned = clean_text(text)
    tokens = word_tokenize(cleaned)
    return [token for token in tokens if token not in stop_words and len(token) > 1]


def main():
    ensure_nltk()
    stop_words = set(stopwords.words("english"))

    faqs = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    processed = []
    for item in faqs:
        combined = f"{item['question']} {item['answer']}"
        processed.append(
            {
                "question": item["question"],
                "answer": item["answer"],
                "tokens": preprocess_text(combined, stop_words),
            }
        )

    OUTPUT_PATH.write_text(json.dumps(processed, indent=2), encoding="utf-8")
    print(f"Saved {len(processed)} processed FAQs to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
