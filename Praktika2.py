def f21(x):
    if x[3]=='xtend':
        if x[0]==2008:
            if x[2]==1959:
                return 0
            elif x[2]==1969:
                return 1
            elif x[2]==1980:
                return 2
        elif x[0]==1974:
            return 3
        elif x[0]==2014:
            if x[2]==1959:
                return 4
            elif x[2]==1969:
                return 5
            elif x[2]==1980:
                return 6
    elif x[3]=='lex':
        return 7
    elif x[3]=='eq':
        if x[0]==2008:
            if x[2]==1959:
                return 8
            elif x[2]==1969:
                return 9
            elif x[2]==1980:
                return 10
        elif x[0]==1974:
            return 11
        elif x[0]==2014:
            return 12

def f22(x):
    e = x&(0x80000000)
    e = e >> 14
    d = x&(0x60000000)
    d = d >> 29
    c = x&(0x1c000000)
    c = c >> 8
    b = x&(0x03fff800)
    b = b >> 9
    a = x&(0x000007ff)
    a = a << 21
    return a | c | e | b | d

def f23(x):
    for i in range(0, len(x)):
        if x[i][0]!=None:
            for j in range(i+1, len(x)):
                if x[j][0]==x[i][0]:
                    x[j] = [None, None, None, None]
    line = 0
    while line!=len(x):
        if x[line][0]==None:
            t=x.pop(line)
        else:
            line=line+1
    for i in range(0, len(x)):
        x[i][0] = x[i][0].replace('@', '[at]')
        x[i][1] = '{} {}'.format(x[i][1][x[i][1].find(' ')+1:], x[i][1][:x[i][1].find(' ')])
        x[i][2] = x[i][2].replace('.', '-')
        x[i][3] = str(round(float(x[i][3]), 1))
    a = [[None for i in range(len(x))] for j in range(len(x[0]))]
    for i in range(0, len(x)):
        for j in range(0, len(x[0])):
            a[j][i] = x[i][j]
    return a