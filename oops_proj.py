class chatbook:
    __user_id = 1 # for static variable/method

    def __init__(self):
        #static variable/method
        self.id = chatbook.__user_id
        chatbook.__user_id +=1

        #Encapsulation
        self.__name = "Default User"

        self.username = ''
        self.password = ''
        self.loggedin = False
        # self.menu()

    # getter and setter
    # def get_name(self):
    #     return self.__name
    
    # def set_name(self,value):
    #     self.__name = value

    #getter and setter for static variable
    def  get_id():
        return chatbook.__user_id
    
    def set_id(val):
        chatbook.__user_id = val


    def menu(self):
        user_input = input(""""Welcome to chatbook!! How would you like to proceed? " \
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message the friend
                           5. Press any other key to exit
                           
                           -> """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.sendmsg()
        else:
            exit() 

    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("Enter your email/username here -> ")
            pwd = input("Enter your password here -> ")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully!!")
                self.loggedin = True
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your messsage here -> ")
            print(f"Following content has been posted -> {txt}")          
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()  

    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input("Whom to send the msg ->     ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("You need to signin first to post something...")
        print("\n")
        self.menu()        
# obj = chatbook()

