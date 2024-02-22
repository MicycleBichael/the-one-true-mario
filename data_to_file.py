
positive = []
control = []

with open('test.txt','r') as f:
    fString = f.read().split('\n')
    for line in fString:
        test_type = line.split(" | ")[0]
        data = line.split(" | ")[2]
        if test_type == "control":
            control.append(data)
        else:
            positive.append(data)

with open("test_machine_readable.txt",'w') as f:
    controlList = " ".join(control)
    posList = " ".join(positive)
    string = f"control:\n{controlList}\npositive:\n{posList}\n\n"
    f.write(string)
    for i, value in enumerate(control):
        f.write(f"{value} & {positive[i]} \\\\\n")
