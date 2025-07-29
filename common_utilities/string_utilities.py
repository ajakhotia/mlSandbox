import os


def string_from_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: File '{file_path}' not found.")

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
