sco=[85,90,78,92,88]
for i in range(len(sco)):
    print(f"scores[{i}] = {sco[i]}")
for score in sco:print(score)
for idx,val in enumerate(sco):
    print(f"Idex{idx}->{val}")
doubled=[x*2 for x in sco]

#array opera
arr=[10,20,30,40]
arr.append(50)
arr.insert(2,55)
arr.extend([60,70])
new_arr=arr+[80,90]
print(new_arr)
