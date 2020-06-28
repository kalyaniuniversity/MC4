import os

def get_filename(file_path):

    """ Returns filename from the path of a file

    Args:
        file_path (string): path of the file

    Returns:
        string: name of the file
    """

    file_name = file_path.split('/')[-1]

    return file_name


def is_valid_path(file_path):

    """Checks if a file path is valid

    Args:
        file_path (string): path of a file

    Raises:
        FileNotFoundError: throws when file path is invalid

    Returns:
        True: when file path is valid
    """

    if os.path.exists(file_path):

        return True
    
    raise FileNotFoundError(f"Could not find {get_filename(file_path)} file!")



    