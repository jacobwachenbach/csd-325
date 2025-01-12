# Jacob Achenbach 11/3/2024 Module 2.2 Fiber Optic
# FOF (Feet of fiber)
# COF (Cost of fiber)
# This program takes user's input and multiplies it to get an output the example was for a fiber optic company.
# Added discounts if the user buys a certain amount

# main function
def main():
    print("Hello welcome to Jacobs fiber optic.")
    COF = .80
    
    # try for input and calculation
    try:
        FOF = int(input("How many feet to do want intstalled? "))

        if FOF >= 500:
            COF = .50
        elif FOF >= 250:
            COF = .70
        elif FOF >= 100:
            COF = .80



        # Times the feet of fiber by the cost of fiber
        FinalCost = FOF * COF
        print(f'The cost will be {FinalCost}. Please consider going with Jacobs fiber optic.')
    # If error try again
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of feet.")


# Run main function.
if __name__ == "__main__":
    main()
