from auth.token import get_token
from setup import *

def main():
    token = get_token(credentials_file_path)
    if not token:
        return

    print(token)


if __name__ == '__main__':
    main()
