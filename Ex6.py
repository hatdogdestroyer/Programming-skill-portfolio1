# Exercise 6: Brute force attack

# Find the correct password for it
correct_password = 54321

max_attempts = 3 # This is the maximum attempts a user can do
attempts = 0 # And this is tha max for the  user

# You have to use a loop to repeat the password until it's correct 
while attempts < max_attempts:
    password = int(input("Enter your password: "))
    
    if password == correct_password:
        print("The Password is correct. Access Granted.")
        break # I put this for the code to stop once i entered the correct password
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        
        if remaining_attempts == max_attempts:
            print("Maximum Tries Reached, Access Denied.")
        else:
            print(f"Incorrect password, you have {remaining_attempts} left")
            
        
        
 
    
 # If a the user reached the maximum attempts then the code will tell the user  