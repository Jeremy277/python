count = 0

while True:
    count += 1
    if count > 10:
        break
    if count == 5:        #跳过5
        continue
    print(count)

input('\n\nPress the enter key to exit.')