import os

if __name__ == '__main__':
    files = os.listdir('.')
    fout = open("files.html", "w")
    for f in files:
        if f[-3:] == 'gif':
            fout.write("<img src = \"%s\"><BR><BR>\n\n"%f)
    fout.close()
