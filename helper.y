import sys

def process_data(data: str) -> str:
    """Processes the input data and returns the result."""
    return data.strip().upper()

def main():
    print("--- Python Script Execution ---")
    
    # Example user input or command-line handling
    if len(sys.argv) > 1:
        input_value = " ".join(sys.argv[1:])
    else:
        input_value = input("Enter input text: ")

    try:
        result = process_data(input_value)
        print(f"Processed Output: {result}")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
