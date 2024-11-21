def main():
    print("Enter numbers to add. Type 'done' when you are finished.")

    numbers = [] 
    while True:
        user_input = input("Enter a number (or 'done' to finish): ").strip()
        
        if user_input.lower() == 'done': 
            break
        
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total = sum(numbers)
    print(f"The numbers you entered are: {numbers}")
    print(f"The total sum is: {total}")

if __name__ == "__main__":
    main()
