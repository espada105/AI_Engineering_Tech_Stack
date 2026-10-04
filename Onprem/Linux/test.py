# this file is only test file
# editing have to use vi
# this file is related to ./logs/test.log, so you can test logs with "python3 test.py >> ./logs/test.log". this means that if you test the file, you can see the logs.

# flush = True -> this is able to making live test

import time

num = int(input())

for n in range(num):
	print(f"{n+1} 번째 테스트 입니다.",flush = True)
	time.sleep(5)

print("end")


