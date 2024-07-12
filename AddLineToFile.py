# 打开目标文件以读取模式，并指定编码为UTF-8
with open('1.txt', 'r', encoding='utf-8') as file:
    # 读取文件的所有行
    lines = file.readlines()

# 打开目标文件以写入模式，并指定编码为UTF-8
with open('1.txt', 'w', encoding='utf-8') as file:
    # 遍历每一行
    for line in lines:
        # 写入当前行到文件
        file.write(line)
        # 添加一个空行
        file.write('\n')