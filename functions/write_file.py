import os

def write_file(working_directory, file_path, content):
    
    #creating an absolute path from the working directory and file path variables
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

   #defining parent dir and determining if within working directory
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    parent_dir = os.path.dirname(abs_file_path)
    os.makedirs(parent_dir, exist_ok = True)
    
    with open(abs_file_path, "w") as f:
        f.write(content)
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    