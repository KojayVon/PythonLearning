import random

years = random.randint(1,10)

num = int(input("请猜猜我的年龄："))

times = 1

while 1:
    if num == years:
        print(f"恭喜你第{times}次就猜对了！")
        break
    else:
        if num > years:
            num = int(input("猜大了，你再猜："))
        else:
            num = int(input("猜小了，你再猜："))
        times += 1
    