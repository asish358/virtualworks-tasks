def greet_user(name: str) -> str:
    """Generates a personalized greeting message."""
    return f"Hello, {name}! Welcome to Python."


def main():
    try:
        # Get input from the user
        user_name = input("Enter your name: ").strip()

        if not user_name:
            print("Name cannot be empty.")
            return

        # Generate and display the greeting
        message = greet_user(user_name)
        print(message)

    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
