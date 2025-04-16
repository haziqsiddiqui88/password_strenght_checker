  
import re 
import streamlit as st
# Password Strenght Checker Conditions:
# 1. At least 8 characters long
# 2. At least one uppercase letter
# 3. At least one lowercase letter
# 4. At least one digit
# 5. At least one special character (e.g., !@#$%^&*)
# 6. No spaces    

# This code checks the strength of a password based on the defined conditions.
def check_password_strength(password):
    if len(password) < 8:
        return " Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return " Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return " Password must contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return " Password must contain at least one digit."
    
    if not re.search(r"[!@#$%^&*]", password):
        return " Password must contain at least one special character (!@#$%^&*)."
    
    if " " in password:
        return " Password must not contain spaces."
    
    return " Password is strong!"

# Streamlit UI
def main():
    st.title("🔐Password Strength Checker ")
    st.markdown("Enter a password below to check if it's strong or weak based on common security rules.")

    password = st.text_input("Enter your password:", type="password")

    if st.button("Check Password"):
        if password:
            result = check_password_strength(password)
            st.info(result)
        else:
            st.warning("Please enter a password.")

if __name__ == "__main__":
    main()
