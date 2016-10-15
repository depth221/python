while(1):
    num_i = input("num: ")
        
    num = float(num_i)
    
    if num > 100:
        exit
    elif num >= 90:
        print("A")
    elif num >= 80:
        print("B")
    elif num >= 70:
        print("C")
    elif num >= 60:
        print("D")
    elif num < 60:
        print("F")
    elif num < 0:
        exit
