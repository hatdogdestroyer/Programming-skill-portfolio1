# Exercise 8: Simple Search

# Write the names that are given
names = ["Tim", "Ian", "Zac", "Ron", "Sam", "Tom"]
# Am allowing the user to display the search term

# You have to get the search term
search_for = input("Enter your name here:")

# Now you can search the name
if search_for in names:
    print(f" {search_for} is in the list.")
else: 
    print(f" {search_for} is not in the list")
# If the user didnt provide input then use "Tom" as the default search term
    
    


