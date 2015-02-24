#!/usr/bin/python3

import os
import string

# Prog to automate renaming of Yify movies in given dir


def main():
    try:
        # change to dir with movie files
        dir_path = input("Please input the dir :  ")
        os.chdir(dir_path)

        # make list of the movie names
        mov_name = []
        mov_name = os.listdir()
        # make a list of words i don't want in the name from this text file
        word_rm = open('/home/lorcan/RENAME/word_rm.txt', 'r')
        word_rm_ls = []

        # making the list of words to be removed
        for line in word_rm:
            word_ls = line.split(',')
            for word in word_ls:
                word = word.strip()
                word_rm_ls.append(word)

        for name in mov_name:
            # split the name into seperate words
            line_list = name.split(".")
            word_list = []
            # only want to change the names for YiFY Movies
            if 'YIFY' in line_list:
                for word in line_list:
                    # only keep the words i want (the actual name and the quality)
                    if word in word_rm_ls:
                        pass
                    elif word.isdigit() is True:
                        pass
                    else:
                        word_list.append(word)

                print('\n****************************************\n\nName changed from |*| ', name, ' |*| to  :  ')
                # take the words in the list of words kept and join them with an _
                short_name = '_'.join(word_list)
                # add the file extension to the end
                new_name = (short_name + '.mp4')
                print('\n\n', new_name, '\n')
                # rename the file
                os.rename(name, new_name)

    except OSError as e:
        print(e)

if __name__ == '__main__':
    main()
