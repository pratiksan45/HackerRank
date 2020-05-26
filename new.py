

total = []
for i in range(int(input())):
    name = input()
    score = float(input())
    name_score = list((score, name))
    total.append(name_score)
print(total)
total.sort()
print(total)
#print(min(total))
#print(total[0][1])
min_mark=total[0][0]
count=0
for i in range(len(total)):
    if min_mark==total[i][0]:
        count= count+1
if count>=1:
    for j in range(count):
        total.pop(0)
print(total)   
now_min_marks=total[0][0]
for k in range(len(total)):
    if now_min_marks==total[k][0]:
        print(total[k][1])
