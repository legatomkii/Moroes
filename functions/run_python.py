import os
import sys
import subprocess
from google import genai

schema_run_python_file = genai.types.FunctionDeclaration(
    name="run_python_file",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(type=genai.types.Type.STRING,
                description="Relative path to the file to be read.",
            ),
            "args": genai.types.Schema(type=genai.types.Type.ARRAY, items=genai.types.Schema(type=genai.types.Type.STRING)),
        },
        required = ["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    file_path_lower = file_path.lower()
    if not file_path_lower.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        completed = subprocess.run([sys.executable, abs_file_path] + args, capture_output=True, timeout=30, cwd=abs_working_dir, text=True)
        if not completed.stdout and not completed.stderr:
            return 'No output produced.'
        result = f'STDOUT: {completed.stdout} STDERR: {completed.stderr}'
        if completed.returncode != 0: 
            result += f' Process exited with code {completed.returncode}'
        return result
    except Exception as e:
        return f'Error: executing Python file: {e}'
    