import os

def is_valid_path(file_path):

    if os.path.exists(file_path):
        return True
    
    raise FileNotFoundError(f"Could not find {get_filename(file_path)} file!")


def get_filename(file_path):

    file_name = file_path.split('/')[-1]

    return file_name
    