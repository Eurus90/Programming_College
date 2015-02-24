#!/usr/bin/python3

import os
import string

''' Prog to automate renaming of Yify movies in given dir '''


def yify(movie_title, bad_words):
    '''takes YIFY movie file names and shortens them to title and quality'''

    # split the name into seperate words
    line_list = movie_title.split(".")
    word_list = []
    # only want to change the names for YiFY Movies
    if 'YIFY' in line_list:
        for word in line_list:
            # only keep the words i want (the actual name and the quality)
            if word in bad_words:
                pass
            elif word.isdigit() is True:
                pass
            else:
                word_list.append(word)

        # take the words in the list of words kept and join them with an _
        short_name = '_'.join(word_list)
        # add the file extension to the end
        sexy_name = (short_name + '.mp4')

    return sexy_name


def aviMKVmp4(name_of):
    '''takes all the other movies and replaces the white space with _'''

    # replace spaces with _
    sexy_name = name_of.replace(" ", "_")

    return sexy_name


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

        # make list of last letters to id file extension
        ext_ls = ['i', 'v', '4', 's']

        # making the list of words to be removed
        for line in word_rm:
            word_ls = line.split(',')
            for word in word_ls:
                word = word.strip()
                word_rm_ls.append(word)

        skip_count = 0
        skip_ls = []

        tot_count = 0

        for name in mov_name:
            tot_count += 1
            nameof = name
            # if YIFY is in the movie filename exe func yify
            if nameof.find(".YIFY") != -1:
                new_name = yify(nameof, word_rm_ls)

            # if the last letter of the filename is in the ext_ls and there are spaces exe func aviMKVmp4
            elif (nameof[-1] in ext_ls) and (nameof.find(" ") != -1):
                new_name = aviMKVmp4(nameof)

            # count the number of files not changed and list the names
            else:
                skip_count += 1
                skip_ls.append(str(tot_count) + '.   ' + nameof)
                continue

            print('\n****************************************\n\n\nName changed from [***|||   ', nameof, '   |||***] to  :  ')
            # rename the file
            os.rename(nameof, new_name)
            print('\n\n', new_name, '\n')

        for title in skip_ls:
            print("\n", title)

    except OSError as e:
        print(e)

if __name__ == '__main__':
    main()
