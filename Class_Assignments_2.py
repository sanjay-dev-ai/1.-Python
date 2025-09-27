class assignment2():
#AIFields
        def Subfields():
            domain = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            print("Sub-fields in AI are:")
            for result in domain:
                print(result)
            return result
#odd/even         
        def oddeven():
            num=int(input("Enter a number:"))
            if(num%2==1):
                print(num,"is Odd Number")
                value="Odd Number"
            else:
                print(num," is Even Number")
                value="Even Number"
            return value
#Marriage Eligiblity
        def Elegible():
            Gender=input("Your Gender:")
            age=int(input("Your Age:"))
            if(Gender=="Male"):
                    if(age<21):
                        print("Not Eligible")
                        criteria="Not Eligible"
                    else:
                        print("Eligible")
                        criteria="Eligible"
                    return criteria
            elif(Gender=="Female"):
                    if(age<18):
                        print("Not Eligible")
                        criteria="Not Eligible"
                    else:
                        print("Eligible")
                        criteria="Eligible"
                    return criteria
#10th Marks and Percentage
        def percentage():
            sub1=int(input("Subject1="))
            sub2=int(input("Subject2="))
            sub3=int(input("Subject3="))
            sub4=int(input("Subject4="))
            sub5=int(input("Subject5="))
            total=sub1+sub2+sub3+sub4+sub5
            print("Total:",total)
            perc=(total/500*100)
            print("Percentage:",perc)
            mark=perc
            return mark
#Area and Perimeter of triangle          
        def triangle():
                num1=int(input("Height:"))
                num2=int(input("Breadth:"))
                print("Area formula:  (Height*Breadth)/2")
                value1=((num1*num2)/2)
                print("Area of Triangle:", value1)
                area=value1
                num3=int(input("Height1:"))
                num4=int(input("Height2:"))
                num5=int(input("Btradth:"))
                print("Perimeter formula: Height1+Height2+Breadth")
                value2=(num3+num4+num5)
                print("Perimeter of Triangle:",value2)
                perimeter=value2
                return area, perimeter
    
    
    
    
        