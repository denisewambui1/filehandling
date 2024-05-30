# file_handling_assignment.py

def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("Line 1: Hello, World!\n")
            file.write("Line 2: The year is 2024.\n")
            file.write("Line 3: This is a sample text file.\n")
        print("File created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error creating/writing to file: {e}")
    finally:
        print("File creation attempt completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
        print("File content:")
        print(content)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error reading file: {e}")
    finally:
        print("File reading attempt completed.")

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Line 4: Appending new content.\n")
            file.write("Line 5: Adding more lines.\n")
            file.write("Line 6: End of appended lines.\n")
        print("Additional content appended successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error appending to file: {e}")
    finally:
        print("File append attempt completed.")

if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()
