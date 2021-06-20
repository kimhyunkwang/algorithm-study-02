inputs = list(map(int, input().split()))
N, score = inputs[0], inputs[1:]

avg = sum(score)/N
overAvg =  list(filter(lambda x: x > avg, score))
print("%.3f"%(round(len(overAvg)/N*100000)/1000.0)+"%")