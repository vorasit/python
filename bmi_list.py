i=1
j=0
name = []
bmi = []
while i <= 3:
    print ("คนที่ : " + str(i))
    n = str(input("ชื่อ = "))
    h = float(input("ส่วนสูง = "))
    w = float(input("น้ำหนัก = "))
    a = h/100
    b = w/(a*a)
    name.append(n)#[0,1,2]
    bmi.append(b)#[0,1,2]
    i+=1
    print ("---------------------")
print ("------------------------------------------")
while j <= 2:
    print("ชื่อ : " + str(name[j]))#[0,1,2]
    print("ค่าเฉลี่ย : " + str(bmi[j]))#[0,1,2]
    if float(bmi[j]) < 18.5 :
        print ("ต่ำกว่าเกณฑ์")
    elif float(bmi[j]) > 18.5 and float(bmi[j]) < 24.9:
        print ("น้ำหนักปกติ")
    elif float(bmi[j]) > 25 and float(bmi[j]) < 29.9:
        print ("อ้วน")
    else :
        print("เกินพิกัด")
    print ("---------------------")
    j+=1
