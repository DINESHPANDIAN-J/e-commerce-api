class website():
    def __init__(self):
        pass
    # save user
    def reg_user(self,register):
        with open("user_details.txt","a") as f:
            f.write(str(register)+"\n")
    # email_validation
    def is_valid_email(self,email):
            # Regular expression for validating an email
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            # Checking the email matches the pattern
            if re.match(pattern, email):
                return True

            print('Enter the valid email address!')
    
    

    # register
    def register(self):
        firstname=input("First Name: ")
        lastname=input("Last Name: ")
        email=input("Email: ")
        verify=self.is_valid_email(email)
        if verify == True:
            password=input("Password: ")
            re_enter_password=input("re-enter password: ")
            if re_enter_password != password :
                re_enter_password=input('Enter Password Correctly!')      

            with open("user_details.json", "a") as f:
                f.write(json.dumps({'first_name':firstname,'last_name':lastname,'email':email,'password':password}))
            
        return f"{firstname} {lastname} details saved successfully!"
    


    def log_in(self):
        user_email=input('Enter your email address:')
        user_password=input('Enter your password:')
        with open('user_details.json') as f:
            users=json.load(f)
        for user in users:
            if user.email == user_email and user.password == user_password:
                print('Welcome to MARLO!')
            else:
                print('invalid user details!')

                
                
        
import re
import json
marlo=website()
marlo.log_in()

