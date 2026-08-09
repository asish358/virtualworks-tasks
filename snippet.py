# A simple script to greet and greet again

def greet(name="world"):
    return f"Hello, {name}!"

# Example usage:
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    if user_name.strip():
        print(greet(user_name))
    else:
        print(greet())
