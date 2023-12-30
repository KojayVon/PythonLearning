hight = int(input("欢迎来到黑马动物园。\n请输入你的身高（cm）："))
VIP = int(input("请输入你的VIP等级："))

if hight >= 120:
    if VIP >= 3:
        print("您的VIP等级为%d，可以免费游玩。" % VIP)
    else:    
        print("您的身高超过120cm，游玩需要补票10元。")
else:
    print("您的身高未超过120cm，可以免费游玩。")

print("祝您游玩愉快。")