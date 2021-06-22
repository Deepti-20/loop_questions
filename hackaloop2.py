def even_odd(even):
    while num>0:
        if num%2==0:
            print("even num")
        else:
            print("odd num")
        num=num-1
    return num
num=int(input("enter any no."))
even_odd(num)