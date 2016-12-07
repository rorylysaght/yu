"""
    Brandon Herford
    06/08/16
    
"""

# Import the random number Python library.
import random

# Define the function that will append a
# random value into the list.
def grid_gen(get_rows):
    """ Input a random value into the list. """
    
    # For each number between 0 and 10.
    for n in range(0, 10):
        
        # Set rand_int to a generated number.
        rand_int = n

        # Add a random int.
        get_rows.append(rand_int)

    # print out the list.       
    print(get_rows)
    
# Define the main function.
def main():
    """ This is the main function. """

    # Set the value of grid_list to an empty list.
    grid_list = []

    # Call the grid_gen funciton.
    grid_gen(grid_list)

    # For every number between 0 and 10,
    # print the grid_list.
    for n in range(0, 12):
        print(grid_list)
        
# Call the main function.   
main()
