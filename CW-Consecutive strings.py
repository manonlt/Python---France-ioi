def longest_consec(strarr, k):
    liste = []
    listelong = []
    listemax = []
    n = len(strarr)
    
    if n == 0 or k > n or k <= 0:
        return ""
    
    else:
        for i in range(n-k+1):
            word = ''
            x = i
            for l in range(k):
                word = word + strarr[x]
                x += 1

            liste.append(word)
            listelong.append(len(word))

        for j in range(len(listelong)):
            if listelong[j] == max(listelong):
                listemax.append(j)

        return liste[listemax[0]]
