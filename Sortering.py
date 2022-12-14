#bruker insertionsort til sortering
def sortering(a):
    for i in range(1, len(a)):
        a0 = i-1
        a1 = a[i]
        while a[a0] > a1 and a0 >= 0:
                a[a0 + 1] = a[a0]
                a0 -= 1
        a[a0 + 1] = a1
    return a

liste = [9,1,2,3,1,12,8]
print(sortering(liste))
print(9)