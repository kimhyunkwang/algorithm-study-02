n = int(input())
members = []

for i in range(n):
    member = input().split()
    member[0] = int(member[0])
    members.append(member)

sorted_members = sorted(members)

for member in sorted_members:
    print(member[0], member[1])