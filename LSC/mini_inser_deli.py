def lcs(a,b,x,y):
    k = [[0 for i in range(y+1)]for i in range(x+1)]
    for i in range(x+1):
        for j in range(y+1):
            if i==0 or j==0:
                k[i][j] = 0
            elif a[i-1]==b[j-1]:
                k[i][j] = k[i-1][j-1]+1
            else:
                k[i][j] = max(k[i-1][j],k[i][j-1])
    return k[x][y]            


def mini_inser_deli(a,b):
    value = lcs(a,b,len(a),len(b))
    print("Mini number of insertion "+ str(len(b)-value))
    print("Mini number of deletion "+ str(len(a)-value))




a = "heap"
b = "pea"
mini_inser_deli(a,b)