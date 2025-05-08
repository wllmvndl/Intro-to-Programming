import math

timer = 0

center = [0,0]

running = True
for _ in range(180):
    timer = timer + 1

    x = (math.cos( math.sqrt(2) * (timer * 180) / math.pi)) - center[0]
    y = (math.sin( math.sqrt(2) * (timer * 180) / math.pi)) - center[1]
    
    print(timer)
    print(x)
    print(y)
    print()
