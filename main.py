from router.intent_router import IntentRouter

def main():
    router = IntentRouter()
    print("Simple Query Router (type 'exit' to quit)")

    while True:
        query = input("\nEnter your question: ")
        if query.lower() == "exit":
            break

        response = router.route(query)
        print(f"Response: {response}")

if __name__ == "__main__":
    main()
