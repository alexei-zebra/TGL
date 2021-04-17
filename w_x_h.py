import subprocess
def w_x_h():
    cols_x_lines = subprocess.run('echo $(tput cols)x$(tput lines)', shell=True, capture_output=True)

    w_not_h = True
    w = ""
    h = ""

#    print(cols_x_lines.stdout)
    for i in str(cols_x_lines.stdout):
#        print(i)
        if i != "b" and i != "'" and i != "x" and i != "\\" and i != "n":
            if w_not_h == True:
                w += str(i)
            elif w_not_h == False:
                h += str(i)
        if i == "x":
            w_not_h = False
#    print(w)
#    print(h)
    w, h = int(h) - 2, int(w)
    return w, h
