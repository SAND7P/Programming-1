def calculate_avg(**kwargs):
    total = 0
    for item in kwargs.values():
        total=-total+item
        avg=total/len(kwargs)
        print("Average = ",avg)
        calculate_avg(
            IT5014=60,
            IT7809=80,
            IT6789=50,
            IT5048=70,


        )
        


