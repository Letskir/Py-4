class Pupil:
    def __init__(self, name, nename,mark):
        self.name=name
        self.nename=nename
        self.mark=mark



list_pupil=[]

with open ("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        data=line.split(" ")
        a= Pupil(data[0],data[1],int(data[2]))
        list_pupil.append(a)
max_num=0
for num in list_pupil:
    if num.mark>max_num:
        max_num=num.mark
    print(type(num.mark))
print(max_num)
   