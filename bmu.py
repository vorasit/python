h = float(input("ส่วนสูง = "))
w = float(input("น้ำหนัก = "))
a = h/100
bmi = w/(a*a)
print(bmi)

if bmi< 18.5 :
    print ("ต่ำกว่าเกณฑ์")
elif bmi >18.5 and bmi < 24.9:
    print ("น้ำหนักปกติ")
elif bmi >25 and bmi <29.9:
    print ("อ้วน")
else :
    print("เกินพิกัด")
