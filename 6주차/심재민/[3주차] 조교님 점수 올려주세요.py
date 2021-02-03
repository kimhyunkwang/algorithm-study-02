# 5주차 알고리즘 스터디 튜터링

n = int(input())
exp = input()
 
global answer
answer = -9999999999
 
num = []
op = []
 
for i in range(n):
    if i % 2 == 0 :
        num.append(int(exp[i]))
    else :
        op.append(exp[i])
 
def cal(a, b, oper):
    if oper == '+':
        return a + b
    elif oper == "-":
        return a - b
    elif oper == "*":
        return a * b
 
def dfs(op_idx, res):
    global answer
 
    if op_idx == len(op):
        if res > answer:
            answer = res
        return None;
 
    dfs(op_idx + 1, cal(res, num[op_idx + 1], op[op_idx]))
 
    if op_idx + 1 < len(op):
        dfs(op_idx + 2, cal(res, cal(num[op_idx + 1], num[op_idx + 2], op[op_idx + 1]), op[op_idx]))
 
dfs(0, num[0])
print(answer)