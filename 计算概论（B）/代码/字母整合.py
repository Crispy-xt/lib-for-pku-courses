word=input()
word=word.lower()
position_list=[]
position=1
letters=[char for char in word]
length=len(word)

for i in range(0,length-1):
    if letters[i+1]==letters[i]:
        position+=1
    else:
        position_list.append(position)
        position += 1
position_list.append(position)

position_list.append(position)
length_1=len(position_list)
for i in range(0,length_1-1):
    if i==0:
        print("("+str(letters[position_list[i]-1])+","+
              str(position_list[i])+")",end="")
    else:
        print("(" + str(letters[position_list[i]-1]) + "," +
              str(position_list[i]-position_list[i-1])+")",end="")





