cgpa=int(input("enter your cgpa:"))
if cgpa>10 or cgpa<0:
    print("invalid cgpa")   
elif cgpa>=6:
    print("eligible for placement")
elif cgpa<=5:
    print("not eligible for placement")