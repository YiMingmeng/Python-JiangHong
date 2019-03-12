def main():
    s = input("请输入一个字符串:")
    output = []
    for i in range(len(s)):
        num = ord(s[i])
        output.append(num)
    print(output)

main()
