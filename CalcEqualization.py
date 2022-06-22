def result(ui):
    list = ui.lineEdit.text().split(" ")


    if list[-1] == '':
        del list[-1]
        del list[-1]

    if list[0] == '':
        list[2] = "-" + list[2]
        del list[0:2]


    for j in range(0, list.count("*")):
        for i in list:
           if i == "*":
                ind = list.index(i)
                list[ind] = float(list[ind-1]) * float(list[ind+1])
                del list[ind-1]
                del list[ind]

    for j in range(0, list.count("/")):
        for i in list:
           if i == "/":
                ind = list.index(i)
                if list[ind+1] == "0":
                    return "Sorry, it's impossible"
                else:
                    list[ind] = float(list[ind-1]) / float(list[ind+1])
                    del list[ind-1]
                    del list[ind]

    for j in range(0, list.count("+")):
        for i in list:
             if i == "+":
                ind = list.index(i)
                list[ind] = float(list[ind-1]) + float(list[ind+1])
                del list[ind-1]
                del list[ind]

    for j in range(0, list.count("-")):
        for i in list:
            if i == "-":
                ind = list.index(i)
                list[ind] = float(list[ind-1]) - float(list[ind+1])
                del list[ind-1]
                del list[ind]

    return list[0]




