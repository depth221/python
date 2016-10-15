while(1):
    try:
        temp_f = input("Enter temp: ")
        temp_c = (float(temp_f) - 32) * (5/9) 
        
        print(temp_f, "℉ =", temp_c, "℃")
    except:
        print("Please enter a number")
