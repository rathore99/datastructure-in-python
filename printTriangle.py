height = int(input())
width = 2**(height) -1

for i in range(height):
    widthtmp = 2**i -1
    str1 = "{:{fill}{align}{width}}"
    str2 = '* '*widthtmp
    print(str1.format(str2,fill=' ',align='^',width= width))
