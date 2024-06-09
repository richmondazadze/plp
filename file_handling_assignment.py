# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("Today's temperature is 25°C.\n")
            file.write("I have 3 apples.\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Error: Permission denied. Cannot create the file.")
    except IOError as e:
        print(f"Error occurred while creating the file: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except IOError as e:
        print(f"Error occurred while reading the file: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This line is appended.\n")
            file.write("Python is awesome!\n")
            file.write("The year is 2024.\n")
        print("\nThree lines appended to 'my_file.txt' successfully.")
    except PermissionError:
        print("Error: Permission denied. Cannot append to the file.")
    except IOError as e:
        print(f"Error occurred while appending to the file: {e}")

def main():
    create_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()