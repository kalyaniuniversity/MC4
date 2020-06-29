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
        Boolean: True, if the file path is valid, otherwise False
    """

    if os.path.exists(file_path):

        return True
    
    raise FileNotFoundError(f"Could not find {get_filename(file_path)} file")


def is_csv(file_path):

    """Checks if a file is csv or not

    Args:
        file_path (string): path of a file

    Returns:
        Boolean: True, if the file format is csv, otherwise False
    """

    file_name = get_filename(file_path)

    if file_name.split('.')[-1] == 'csv':
        return True

    return False



    