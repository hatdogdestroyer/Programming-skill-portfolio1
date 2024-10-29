# Exercise 4: Primitive Quiz

# List down the European Countires and their capitals
countries_and_capitals = [
    ("United Kingdom","London"),
    ("Norway","Oslo"),
    ("Italy","Rome"),
    ("Spain","Madrid"),
    ("Denmark","Copenhagen"),
    ("Poland","Warsaw"),
    ("Sweden","Stockholm"),
    ("Germany","Berlin"),
    ("Finland","Helsinki"),
    ("France","Paris"),
]

# Initializing score
score = 0

# Now you have to start the quiz
# Loop each country and their capitals
for country, capital in countries_and_capitals:
    print(f"What is the capital of {country}?")
    answer = input().lower()
    
    # Now you have to check if your answer is correct
    if answer == capital.lower():
        print("Correct!")
        score += 1
    else:
            print(f"Incorrect. The capital of {country} is {capital}.")
            # This is given when your answer is incorrect 
            
# You can now print the final score
print("------------------------")
print(f"you scored {score} out of {len(countries_and_capitals)}")


        
        