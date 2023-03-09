with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/4/Day4.txt") as f:
    data = f.readlines()

message = {}
for item in data:
    if item[:4] != "5555":
        continue
    # print("freger")
    sennum = item[4:12]
    seqnum = item[12:14]
    checksum = item[14:16]
    content = item[16:]
    checktotal = 0
    for x in range(len(content)//2):
        byte = content[2*x] + content[2*x+1]
        checktotal += int(byte, 16)
    # print(checktotal, checksum)
    if checktotal%256 == int(checksum, 16):
        messagestr = ""
        for x in range(len(content)//2):
            byte = content[2*x] + content[2*x+1]
            letter = chr(int(byte, 16))
            messagestr += letter
        position = str(int(seqnum, 16))
        message[position] = messagestr


# print(message)
final = ""
for x in sorted(message.keys()):
    final += message[x]


print(final)

