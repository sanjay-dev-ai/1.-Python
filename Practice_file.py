class multifunction():
    def oddeven():
        num = int(input("Enter the number:"))
        if((num % 2) == 0):
            print("Even number")
            status = "Even Number"
        else:
            print("Odd number")
            status = "odd number"
        return status
    def BMI():
        value = int(input("Enter the Weight:"))
        if(value<18):
            print("Under Weight")
            message="Under Weight"
        elif(value<=24):
            print("Normal Weight")
            message="Normal Weight"
        elif(value<=30):
            print("Over Weight")
            message="Over Weight"
        else:
            print("Very Over Weight")
            message="Very Over Weight"
        return message