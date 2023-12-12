import os

def write_file(file_name, file_content):
    # Add a file extension (e.g., ".txt") to the file_name
    file_name_with_extension = file_name + ".txt"

    try:
        # Open the file for writing, creating any necessary directories
        os.makedirs(os.path.dirname(file_name_with_extension), exist_ok=True)
        with open(file_name_with_extension, "w") as file:
           
            file.write(file_content)
        print(f"File '{file_name_with_extension}' has been successfully written.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file(file_name, file_content):
   
    file_name_with_extension = file_name + ".txt"

    try:
       
        with open(file_name_with_extension, "a") as file:
            
            file.write(file_content)
        print(f"Content has been successfully appended to '{file_name_with_extension}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(file_name):
    
    file_name_with_extension = file_name + ".txt"

    try:
        
        with open(file_name_with_extension, "r") as file:
            
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{file_name_with_extension}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_file(file_name):
    pass
