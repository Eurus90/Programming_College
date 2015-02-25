import os
import string


def main():
    try:
        orgdir = input("Please input the dir :  ")
        os.chdir(orgdir)

        file_ls = []
        file_ls = os.listdir()

        ext_ls = ['i', 'v', '4']

        for name in file_ls:
            fold_nm = name
            newdir = str(orgdir + '/' + fold_nm)
            try:
                os.chdir(newdir)
                newfl_ls = []
                newfl_ls = os.listdir()
                for fl_nm in newfl_ls:
                    if fl_nm[-1] in ext_ls:
                        os.rename(newdir + '/' + fl_nm, orgdir + '/' + fl_nm)
                        print('\n\n-- ', fl_nm, '\n\n FROM  :', newdir, '\n\n   TO  :', orgdir, '\n\n')
                    else:
                        continue

            except OSError as E:
                continue

    except OSError as e:
        print(e)


if __name__ == '__main__':
    main()
