def ot(n):
    m = len(n)
    lst1 = []
    lst2 = []

    for i in range(0, m - 2):
        for j in range(i + 1, m-1):
            lst1.append(n[i])
            if lst1[len(lst1)-1] < n[j]:
                lst1.append(n[j])
            for l in range(j + 1, m):
                if n[l] > lst1[len(lst1)-1]:
                    lst1.append(n[l])

            if len(lst1) > len(lst2):
                lst2 = lst1
            lst1 = []
    return lst2

n = [3,4,9,7,2,3,4,9]
print("A lista hossza: ", len(ot(n)), ot(n))


