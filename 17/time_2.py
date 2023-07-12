import time


for h in range(0, 24):
    for m in range(0, 60):
        for s in range(0, 60):
            print(h, " ", m, " ", s, end="\r")
            time.sleep(1)

