import os


def read_secret(secret_filename: str) -> str:
    current_dir = os.path.dirname(__file__)
    secret_file_path = os.path.join(current_dir, secret_filename)

    try:
        with open(secret_file_path, 'r') as file:
            secret = file.read().strip()
            return secret

    except FileNotFoundError:
        raise FileNotFoundError(f'Cannon find the secret at {secret_file_path}')

    except Exception as error:
        raise Exception(f'An error occurred while attempting to read {secret_file_path}. Error: {error}')
