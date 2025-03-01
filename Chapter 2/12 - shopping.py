shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

"""
This script defines a shopping list and iterates through it to print out items to buy, excluding 'spam'.
The script contains two versions of the iteration:
1. The first version (commented out) uses an if statement to check if the item is not 'spam' before printing it.
2. The second version (active) uses a for loop with a continue statement to skip over 'spam' and print the rest of the items.
The 'continue' statement is used to skip the current iteration of the loop when the item is 'spam', effectively ignoring 'spam' in the output.
"""
 
for item in shopping_list:
    if item == "spam":
        break    
    
    print("Buy " + item)
    