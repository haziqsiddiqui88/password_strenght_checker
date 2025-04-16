  
import re 

# Password Strenght Checker Conditions:
# 1. At least 8 characters long
# 2. At least one uppercase letter
# 3. At least one lowercase letter
# 4. At least one digit
# 5. At least one special character (e.g., !@#$%^&*)
# 6. No spaces    

# This code checks the strength of a password based on the defined conditions.
def check_password_strength(password):  #pass password as a parameter

    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*]", password):
        return "Password must contain at least one special character."
   
    return "Password is strong."

def password_checker():
   print("Welcome to the Password Strength Checker!")

   while True:   
         password = input("Please enter a password to check its strength: ")
         result = check_password_strength(password) #Call password as a arguement
         print(result)
    
         if result == "Password is strong.":
                print("Thankyou for using this tool!")
                break
         
         
if __name__ == "__main__":
    password_checker()       

