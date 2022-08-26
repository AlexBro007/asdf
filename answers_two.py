#4. Исключения

#(1)
answers = {
    "hello": "yo man!",
    "how is it going": "im fine, and you?",
    "bye": "cya.",
}

def get_answer(question, answers):
    return answers.get(question)


def ask_user(answers):
    while True:
        try:
            user_input = input("say something: ")
            answer = get_answer(user_input, answers)
            print(answer)

            if user_input == "bye":
                break
        except KeyboardInterrupt:
            print("\noh no, you are quiting =c...\nits so sad ;c")
            break

ask_user(answers)
