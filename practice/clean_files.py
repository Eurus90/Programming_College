import os
import string


def main():
    try:
        dir_path = input("Please input the dir :  ")
        os.chdir(dir_path)

        file_ls = []
        file_ls = os.listdir()

        print(file_ls)



    except OSError as e:
        print(e)


if __name__ == '__main__':
    main()
