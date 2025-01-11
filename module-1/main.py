# Jacob Achenbach 1/11/2025 Module 1.3 Assignment

# A song that counts how many beers are the on the wall and everytime it will subtract 1 and sing it again
# When it gets to one it will prompt the user to buy more


def countdown_bottles(num_bottles):
    # Loop through the number of bottles, counting down to 0
    for i in range(num_bottles, 0, -1):
        if i > 1:
            # Print lyrics for more than 1 bottle
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i - 1} bottle{'s' if i - 1 > 1 else ''} of beer on the wall.")
        else:
            # Print lyrics for the last bottle of the song
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
    # Print the ending lyrics and to go buy more beer
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

def main():
    # Prompt the user for the number of bottles
    try:
        num_bottles = int(input("Enter number of bottles: "))
        if num_bottles > 0:
            # Call the countdown function if input is valid
            countdown_bottles(num_bottles)
        else:
            # Handle case where input is not a positive number
            print("Please enter a positive number.")
    except ValueError:
        # Handle case where input is not a number
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    # Run the main function
    main()