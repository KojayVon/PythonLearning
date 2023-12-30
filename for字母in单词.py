zfc = input("请输入字符串：")
zm = input("请输入要查询的字母：")
times =  0

j = ord(zm)

for k in zfc:
    i = ord(k)
    if j == i:
        times += 1
    elif (j == (i + 32)) & (j >= 97) & (j <= 122):
        times += 1
    elif (j == (i - 32)) & (j >= 56) & (j <= 90):
        times += 1

print(f"您查询的字母\"{zm}\"在该单词\"{zfc}\"中出现了{times}次。")
