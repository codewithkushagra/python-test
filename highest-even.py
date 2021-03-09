def highest_even(l):
    for i in l:
        if i%2==0:
            continue
        else:
            l.remove(i)
    return l


l=[1,2,1,4,5,6,4,8,9,10,11]

print(highest_even(l))