#!/usr/bin/python3

import os
import string

# Prog to rename all files in given dir


def main():
    try:
        # change to dir with movie files
        dir_path = input("Please input the dir :  ")
        os.chdir(dir_path)

        # make list of the movie names
        mov_name = []
        mov_name = os.listdir()

        count = 0

        for name in mov_name:
            count += 1
            # print the org file name
            print("\n\n****************************************************\n\n", name, "          ", count, " of ", len(mov_name), "\n\n")

            # ask the user if they would like to change the org name
            yes_no = input("Rename the file [ 'y' ( YES ) / 'n' ( NO ) / 'c' ( CLOSE )] :  ")

            while yes_no != "y" and yes_no != "n" and yes_no != "c":
                yes_no = input("You MUST enter 'y' or 'n' or 'c' :  ")

            else:
                if yes_no == 'y':
                    new_name = input("Rename  :  ")
                    os.rename(name, new_name)
                elif yes_no == 'n':
                    continue
                else:
                    break

    except os.OSError as e:
        print(e)

if __name__ == '__main__':
    main()
