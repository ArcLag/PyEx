IP = (input("Enter here your IP Address: "))
IP += '.'
segment = 1
segmentLength = 0

for char in IP:
    if char == '.':
        print("segment {} contains {} characters.".format(segment, segmentLength))
        segment += 1
        segmentLength = 0
    else:
        segmentLength += 1

if char != '.':
    print("segment {} contains {} characters.".format(segment, segmentLength))


