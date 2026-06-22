print("โปรแกรมคำนวนคะแนนรวม")

Biology = int(input("กรอกคะแนนวิชาชีวะ \n"))
chemical = int(input("กรอกคะแนนวิชาเคมี \n"))
math = int(input("กรอกคะแนนวิชาคณิตศาสตร์ \n"))

Total_score = Biology + chemical + math
averag =  (Biology + chemical + math)/3

print("คะแนนรวม ; ",Total_score, )

print("คะแนนเฉลี่ย ; ",averag, )

if averag <60:
    print("คะแนนรวมของคุณคือ" , averag)
    print("ควรปรับปรุง")
elif averag <80:
    print("คะแนนรวมของคุณคือ" , averag)
    print("ผ่าน")
else:
    print("คะแนนของคุณคือ" , averag)
    print("ดีเยี่ยม")