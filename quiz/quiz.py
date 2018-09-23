def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit game")
    
    option = input("Enter option: ")
    return option

def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines): #creates a tuple in memory with a line number at begining
        if i % 2 == 0: #if number us even its a question
            questions.append(text)
        else:
            answers.append(text) #if not even it is an answer
            
    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers) #so doesnt need to zip everytime loop is run
    
    score = 0
    
    for question, answer in questions_and_answers: 
        guess = input(question + " > ")
        #check answer and update score
        if guess == answer:
            score += 1
            print("Correct!")
            print(score)
        else:
            print("Wrong!")
            
    print("You got {0} out of {1} correct".format(score, number_of_questions))

def add_question():
    print("")
    question = input("Enter a question\n> ")
    
    print("")
    print("Ok then, tell me the answer")
    answer = input("{0}\n> ".format(question))
    
    file = open('questions.txt', 'a')
    file.write(question + "\n")
    file.write(answer +"\n")
    file.close()
    
def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
        elif option == "2":
            add_question()
        elif option == "3":
            break
        else:
            print("Invalid option")
        print("")
        
game_loop()
