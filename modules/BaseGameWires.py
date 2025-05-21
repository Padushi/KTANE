def subjectOfWires():
    serial = input("Input Serial Number")
    wires = input("Input Your wires")
    #   B = Blue, R = Red, Y = Yellow Q = Black, W = White
    n = len(wires)
    colors = [0,0,0,0,0,]
    for i in range(len(wires)):
        if wires[i] == "B":
            colors[1] += 1
        if wires[i] == "R":
            colors[2] += 1
        if wires[i] == "Y":
            colors[3] += 1
        if wires[i] == "Q":
            colors[4] += 1
        if wires[i] == "W":
            colors[5] += 1
    print(colors)
subjectOfWires()
