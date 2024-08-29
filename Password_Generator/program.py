import random
import string

def generate_password(length):
    # Define the character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Prompt the user for the length of the password
    while True:
        try:
            length = int(input("Enter length of the password: "))
            if length < 1:
                raise ValueError("Length must be at least 1.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a positive integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

# Run the password generator
if __name__ == "__main__":
    main()
