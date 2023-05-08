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
            while re_enter_password != password :
                re_enter_password=input('Enter Password Correctly!')   
            with open('user_details.json', 'r') as f:
                user_details = json.load(f) 
            user_details.append({'first_name':firstname,'last_name':lastname,'email':email,'password':password})
            with open("user_details.json", "w") as f:
                json.dump(user_details,f)
            
        return f"{firstname} {lastname} details saved successfully!"
    


    def log_in(self):
        user_email=input('Enter your email address:')
        user_password=input('Enter your password:')
        with open('user_details.json','r') as f:
            user_details=json.load(f)
        for user in user_details:
            count=0
            if user['email'] == user_email and user['password'] == user_password:
                print('Welcome to MARLO!')
                product=list(input('Enter the name of the product you have bought: ').split(' '))
                user['product_purchased'] = product
                with open('user_details.json','w') as f:
                    json.dump(user_details, f)
                count += 1
                break

            if count ==0:
                print('invalid user details!')
        
    
            



    def adminlog(self):
        admin_id=input('Enter the admin_id: ')
        admin_code=input('Enter the admin_code: ')
        with open('admin.json', 'r') as f:
            admin_details=json.load(f)
        for admin in admin_details:
            if admin['admin_id'] == admin_id and admin['codeword']==admin_code:
                print('Welcome guru Ji!')
                csv_file = input("Enter csv filepath name you want to upload:")
# Open the CSV file
                with open(csv_file, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    with open('product_whole.csv', 'w', newline='') as outfile:
                        writer = csv.writer(outfile)
                        for row in reader:
                            writer.writerow(row)

    

                        
                    



                        

    
                
                
        
import re
import os
import json
import csv
marlo=website()
print("select the option you want to do:'\n'1.Already have an Account '\n'2.New user '\n'3.Admin user '\n'4.product view")
option=int(input())
if option == 1:
    marlo.log_in()
if option == 2:
    marlo.register()
if option == 3:
    marlo.adminlogin()

