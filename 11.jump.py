print("โปรแกรมช่วยคำนวณคะแนนรวม") 

point1 = int(input("กรอกคะแนนวิชาที่1: ")) 

point2 = int(input("กรอกคะแนนวิชาที่2: ")) 

point3 = int(input("กรอกคะแนนวิชาที่3: ")) 

total_point = point1 + point2 + point3 

print("คะแนนรวมของคุณคือ:", total_point) 

if total_point >= 80 : 
    print("ระดับคะแนน: ดีเยี่ยม") 

elif total_point >= 60 : 
    print("ระดับคะแนน: ผ่าน") 
    
else: 
    print("ระดับคะแนน: ควรปรับปรุง")
