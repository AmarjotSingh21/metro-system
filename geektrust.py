from sys import argv
from src.main import run


def main():
    expect_args_length: int = 2
    if len(argv) != expect_args_length:
        raise Exception("File path not entered")
    file_path = argv[1]

    with open(file_path, 'r') as f:
        lines = f.readlines()
        run(lines)


if __name__ == "__main__":
    main()
