import random as rm
import string as str
from datetime import datetime

login_user = ''
marks = 0
login_status = False
quiz_topic = ''
def main():
    print()
    print(f"{'#'*30}\n{'*'*9} QUIZ SYSTEM {'*'*8}\n{'#'*30}")
    ch = input("""
    Choose your choice:
    1. Register
    2. Login
    3. Exit
    Enter your choice: """)
    if ch == '1':
        register()
    elif ch == '2':
        login()
    elif ch == '3':
        exit_()
    else:
        print(f"{'#'*70}")
        print("You choosed incorrect option please choose correct option!!").upper()
        print(f"{'#'*70}")


def register():
    print()
    print("----------------------------------------------------")
    print(f"{'#'*10} WELCOME TO QUIZ REGISTER PAGE {'#'*10}")
    print("-----------------------------------------------------------------")
    print("REGISTER HERE, Fill your details and explore the world of Quiz!!!")
    print("-----------------------------------------------------------------")
    name = input("Enter your name: ").upper()
    email = input("Enter your email id: ")
    print("---------------------------------------")
    print("CONTACT NUMBER SHOULD BE OF 10 DIGIT !!")
    print("---------------------------------------")
    contact = input("Enter your contact number: ").strip()
    while (len(contact) < 10 or len(contact) >10):
        print("\nInvilid contact number!!")
        contact = input("Enter your valid mobile number: ")
        
    print("\n-----------------------------------------------------")
    print("LENGTH OF PASSWORD SHOULD BE OF 6 CHARACTER OR MORE !!")
    print("-----------------------------------------------------")
    pwd = input("Enter your password: ")
    while(len(pwd) < 6):
        print("\nYou have entered too short password!!,Please Enter Password of 6 or more characters!")
        pwd = input("Enter your password again: ")
        
    l = str.ascii_lowercase
    u = str.ascii_uppercase
    d = str.digits
    rl = rm.sample(l,2)
    ru = rm.sample(u,1)
    rd = rm.sample(d,2)

    username = (rl + ru + rd)
    rm.shuffle(username)
    username = ''.join(username)
    username = name.lower() + username

    register_data = f"{name},{email},{contact},{username},{pwd}"
    login_data = f"{username},{pwd}"

    with open('user_details.txt','a') as file:
        file.write(register_data)
        file.write("\n")
    with open('login_details.txt','a') as file:
        file.write(login_data)
        file.write("\n")
    print("----------------------------------------------------------------------------------------------------------")
    print(f"Hello! {name}, your username is {username} and password is {pwd}, PLEASE SAVE IT FOR FUTURE LOGIN!!")
    print("----------------------------------------------------------------------------------------------------------")
    CH = input("Do you want to login and attempt quiz y/n: ").lower()
    print("-----------------------------------------------")
    if CH == ('y' or 'yes'):
        login()
    else:
        print("Thanks! for register here!!!")
        exit()


def login():
    global login_user
    global login_status
    print("\n-------------------------------------------------")
    print(f"{'#'*10} WELCOME, TO QUIZ LOGIN PAGE {'#'*10}")
    print("-------------------------------------------------------------")
    print("LOGIN HERE, Fill your details and explore the world of Quiz!!")
    print("-------------------------------------------------------------")

    choice = input("""
    1. If you have register earliear please slect login option 1.
    2. If you haven't register with us please register yourself option 2.\n
    Choose your choice 1 or 2 : """)
    if choice == '1':
        print("\n-------------------------------------------------")
        print(f"{'#'*10} WELCOME, TO QUIZ LOGIN PAGE {'#'*10}")
        print("-------------------------------------------------")
        print("LOGIN HERE, Fill your details and explore the world of Quiz!!")
        print("-------------------------------------------------------------")
        username = input("Enter your username: ")
        user = []
        userpass = {}
        with open('login_details.txt','r') as file:
            data = file.readlines()
            for i in data:
                da = i.split(',')
                ps = da[-1].replace('\n','')
                userpass[da[0]] = ps
                user.append(da[0])
        if username in user:
            pwd = input("Enter your password: ")
            if pwd in userpass[username]:
                print("\n-------------------------------------------------------------")
                print(f"WELCOME!! User {username} you Logged in suncessfully!!")
                print("-------------------------------------------------------------")
                login_status = username
                with open('user_details.txt','r') as file:
                    data = file.readlines()
                    for i in data:
                        da = i.split(',')
                        if username == da[3].strip():
                            login_user = da[0]
                    after_login()
            else:
                print(f"Hello!! {login_user}, you have entered wrong password please do login again!!")
                login()
        else:
            print("PLEASE ENTER CORRECT USERNAME OR FIRST REGISTER YOURSELF!!")
            login()
    elif choice == '2':
        register()
    else:
        print("PLEASE CHOOSE CORRECT OPTION!!")
        login()


def after_login():
    ch = input("""
    Select an option for process:
          1. Attempt Quiz.
          2. Show Result.
          3. See profile.
          4. Main menu.
          5. Exit.
          Enter your choice: """)
    if ch == '1':
        attempt_quiz()
    elif ch == '2':
        show_result()
    elif ch == '3':
        show_profile()
    elif ch == '4':
        main()
    elif ch == '5':
        exit_()
    else:
        print("Please select correct option!!")
        after_login()


def attempt_quiz():
    global login_user
    global quiz_topic
    print()
    print("*"*40)
    print(f"Hello {login_user.upper()} Welcome in Quiz. GOOD LUCK!")
    print("*"*40)
    print()
    quiz_choice = input("Please select an category to attempt quiz: \n 1. Python\n 2. Java\n 3. C/C++\n Enter your option: ")
    if quiz_choice == '1':
        quiz_topic = "PYTHON"
        python_quiz()

    elif quiz_choice == '2':
        quiz_topic = "JAVA"
        java_quiz()

    elif quiz_choice == '3':
        quiz_topic = "C/C++"
        c_quiz() 
    else:
        print("Please Choose correct quiz option: ")
        attempt_quiz()

def python_quiz():
    global quiz_topic
    global login_user
    global marks
    print(f"Hello {login_user} Welcome in {quiz_topic} Quiz.")
    print()
    
    with open('python.txt','r') as file:
        data = file.readlines()
        que = rm.sample(data,5)

        q = 1
    
    for i in range(len(que)):
        da = que[i].split(',')
        print(f"Que {q}: {da[0]}")
        print(f"A. {da[1]}\nB. {da[2]}\nC. {da[3]}\nD. {da[4]}")

        ans = input("Enter your answer option A/B/C/D : ").lower()
        print()
        res = da[-1].replace('\n','')
        if ans == res:
            marks += 1
        q += 1
    percentage = (marks/5)*100
    da = datetime.now()
    quiz_time = da.strftime("%d %m %Y %H:%M:%p")

    final_result = f"{login_user},{percentage},{quiz_topic},{quiz_time}"
    with open('quiz_resutl.txt','a') as file:
        file.write(final_result)
        file.write("\n")

    print(f"Hello {login_user} Thanks for attempt MCQ Quiz You obtain {marks} marks out of 5.")
    print(f"{'#'*10} CORRECT ANSWERS: {'#'*10}")

    s = 1
    for i in range(len(que)):
        da = que[i].split(',')
        ans = ''
        an = da[-1].replace("\n",'')
        if an == 'a':
            ans = da[1]
        elif an == 'b':
            ans = da[2]
        elif an == 'c':
            ans = da[3]
        elif an == 'd':
            ans = da[4]
        else:
            ans = ans
        print(f"Que.{s}: {da[0]}, ⁕ANS ->> {ans}")
        s += 1


def java_quiz():
    global quiz_topic
    global login_user
    global marks
    print(f"Hello {login_user} Welcome in {quiz_topic} Quiz.")
    print()
    
    with open('java.txt','r') as file:
        data = file.readlines()
        que = rm.sample(data,5)
        q = 1
    
    for i in range(len(que)):
        da = que[i].split(',')
        print(f"Que {q}: {da[0]}")
        print(f"A. {da[1]}\nB. {da[2]}\nC. {da[3]}\nD. {da[4]}")

        ans = input("Enter your answer option A/B/C/D : ").lower()
        print()
        res = da[-1].replace('\n','')
        if ans == res:
            marks += 1
        q += 1
    percentage = (marks/5)*100
    da = datetime.now()
    quiz_time = da.strftime("%d %m %Y %H:%M:%p")

    final_result = f"{login_user},{percentage},{quiz_topic},{quiz_time}"
    with open('quiz_resutl.txt','a') as file:
        file.write(final_result)
        file.write("\n")

    print(f"Hello {login_user} Thanks for attempt MCQ Quiz You obtain {marks} marks out of 5")
    print(f"{'#'*10} CORRECT ANSWERS: {'#'*10}")

    s = 1
    for i in range(len(que)):
        da = que[i].split(',')
        ans = ''
        an = da[-1].replace("\n",'')
        if an == 'a':
            ans = da[1]
        elif an == 'b':
            ans = da[2]
        elif an == 'c':
            ans = da[3]
        elif an == 'd':
            ans = da[4]
        else:
            ans = ans
        print(f"Que.{s}: {da[0]}, ANS: {ans}")
        s += 1
    
def c_quiz():
    global quiz_topic
    global login_user
    global marks
    print(f"Hello {login_user} Welcome in {quiz_topic} Quiz.")
    print()
    
    with open('c.txt','r') as file:
        data = file.readlines()
        que = rm.sample(data,5)
        q = 1
    
    for i in range(len(que)):
        da = que[i].split(',')
        print(f"Que {q}: {da[0]}")
        print(f"A. {da[1]}\nB. {da[2]}\nC. {da[3]}\nD. {da[4]}")

        ans = input("Enter your answer option A/B/C/D : ").lower()
        print()
        res = da[-1].replace('\n','')
        if ans == res:
            marks += 1
        q += 1
    percentage = (marks/5)*100
    da = datetime.now()
    quiz_time = da.strftime("%d %m %Y %H:%M:%p")

    final_result = f"{login_user},{percentage},{quiz_topic},{quiz_time}"
    with open('quiz_resutl.txt','a') as file:
        file.write(final_result)
        file.write("\n")

    print(f"Hello {login_user} Thanks for attempt MCQ Quiz You obtain {marks} marks out of 5")
    print(f"{'#'*10} CORRECT ANSWERS: {'#'*10}")

    s = 1
    for i in range(len(que)):
        da = que[i].split(',')
        ans = ''
        an = da[-1].replace("\n",'')
        if an == 'a':
            ans = da[1]
        elif an == 'b':
            ans = da[2]
        elif an == 'c':
            ans = da[3]
        elif an == 'd':
            ans = da[4]
        else:
            ans = ans
        print(f"Que.{s}: {da[0]}, ANS: {ans}")
        s += 1
    

def show_result():
    global login_user
    with open('quiz_resutl.txt','r') as f:
        u_data = f.readlines()
        for i in u_data:
            da = i.split(',')
            da[-1].replace('\n','')    
            if da[0] == login_user:
                print()
                print(" ----------------------------------------------")
                print(" |               QUIZ SYSTEM                  ")
                print(" |                  Result                    ")
                print(" ----------------------------------------------")
                print(" | Name :",da[0])
                print(" | Quiz topic :",da[2])
                print(" | Quiz time & date :",da[3],end="")
                print(" | Marks in percentage  :",da[1],"%")
                print(" ----------------------------------------------\n")
                ch = input("Do you want to go previous menu y/n: ").lower()
                if ch == ('y' or 'yes'):
                    after_login()
                elif ch == ('n' or 'no'):
                    exit_()
                break
            else:
                print("-----------------------------------------------")
                print(f"Hey! {login_user} you haven't attempt any quiz.")
                print("-----------------------------------------------")
                at = input("Do you want to attempt Quiz y/n: ").lower()
                print("-----------------------------------------------")
                if at == ('y' or 'yes'):
                    attempt_quiz()
                elif at == ('n' or 'no'):
                    print(f"Thanks for using our Quiz system!! {login_user}, have a great day ahead!!")
                    print("-----------------------------------------------")
                    exit_()
                break

def show_profile():
    global login_user
    with open('user_details.txt','r') as f:
        u_data = f.readlines()
        for i in u_data:
            da = i.split(',')
            da[-1].replace('\n','')    
            if da[0] == login_user:
                print()
                print(" ----------------------------------------------")
                print(" |               QUIZ SYSTEM                  ")
                print(" |                 Profile                    ")
                print(" ----------------------------------------------")
                print(" | Name :",da[0])
                print(" | Email id :",da[1])
                print(" | Mobile number :",da[2])
                print(" | User id  :",da[3])
                print(" ----------------------------------------------")

                ch = input("Do you want to go to previous menu y/n: ")
                if ch == ('y' or 'yes'):
                    after_login()
                elif ch == ('n' or 'no'):
                    exit_() 

def exit_():
    global login_status
    print("--------------------------------------------------------------------------------------------")
    ch = input("IF you want to access quiz system again press y, or if you want to close the quiz press n: ").lower()
    print("--------------------------------------------------------------------------------------------")
    if ch == 'y' or ch == 'yes':
        main()
    else:
        print("------------------------------------------------------")
        print("THANKS TO VISIT OUR QUIZ SYSTEM, PLEASE VISIT AGAIN!!!")
        print("------------------------------------------------------")
        login_status = False
        exit()

if __name__ == "__main__":
    main()