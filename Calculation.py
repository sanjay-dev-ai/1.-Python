class multifunction():
    def oddeven():
        num=int(input("Enter the number:"))
        if(num%2==1):
            print("Odd Number")
            value="Odd Number"
        else:
            print("Even Number")
            value="Even Number"
        return value
    def BMI():
        value=int(input("Enter the BMI Index:"))
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