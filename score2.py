while True:
    try:
        num = input("num: ")

        if num == "½":
            num = 1/2
        elif num == "⅓":
            num = 1/3
        elif num == "⅔":
            num = 2/3
        elif num == "¼":
            num = 1/4
        elif num == "¾":
            num = 3/4
        elif num == "⅛":
            num = 1/8
        elif num == "⅜":
            num = 3/8
        elif num == "⅝":
            num = 5/8
        elif num == "⅞":
            num = 7/8
        
        num = float(num)
        if num > 1.0 or num < 0.0:
            print("Bad score")
        elif num >= 0.9:
            print("A")
        elif num >= 0.8:
            print("B")
        elif num >= 0.7:
            print("C")
        elif num >= 0.6:
            print("D")
        elif num >= 0.0:
            print("F")
        else:
            print("Bad score")
    except:
        print("Bad score")
            
