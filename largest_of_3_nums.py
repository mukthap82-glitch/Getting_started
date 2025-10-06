def largest(*args):
    length = len(args)
    count=0
    max = 0
    for i in args:
        if(count==0):
            max = i
            count = count+1
        else:
            if(i>max):
                max = i
    print(f"The largest number is :{max}")

largest(10,6,12)                


