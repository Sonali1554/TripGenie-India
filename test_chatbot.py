from rag.chatbot import ask_question

while True:

    query = input("\nAsk: ")

    if query.lower() == "exit":
        break

    answer = ask_question(query)

    print("\nAnswer:")
    print(answer)