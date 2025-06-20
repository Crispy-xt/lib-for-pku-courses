from collections import defaultdict
team_numbers=0
s=set()
ac_num=defaultdict(int)
submit_num=defaultdict(int)
ac_list=defaultdict(list)
for _ in range(int(input())):
    team,problem,result=input().split(',')
    s.add(team)
    submit_num[team]+=1
    if result=='yes':
        if problem not in ac_list[team]:
            ac_num[team]+=1
            ac_list[team].append(problem)
information=[]
for team in s:
    information.append((-ac_num[team],submit_num[team],team))
information.sort()
n=min(12,len(s))
for i in range(n):
    ac,submit,team=information[i]
    print(f"{i+1} {team} {-ac} {submit}")