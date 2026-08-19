from src.retrieve import retrieve

# 10 realistic questions a FastAPI user might ask
QUESTIONS = [
    "how do I install FastAPI?",
    "how do I add a dependency injection?",
    "how does FastAPI handle request validation?",
    "how do I declare a path parameter?",
    "how do I handle CORS?",
    "how do I return a JSON response?",
    "how do I use OAuth2 for security?",
    "how do I handle background tasks?",
    "how do I test my FastAPI app?",
    "how do I deploy FastAPI?",
]


def main():
    for q in QUESTIONS:
        print("=" * 70)  # a separator line, 70 chars wide
        print("Q:", q)
        hits = retrieve(q, k=3)
        for rank, h in enumerate(hits, start=1):
            snippet = h["text"][:60].replace("\n", " ")
            print(f"  #{rank} [dist {h['distance']}] {h['source']}: {snippet}")


if __name__ == "__main__":
    main()
