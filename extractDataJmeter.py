testFile2 = open("/home/gwthamy/Desktop/Task2/jmeterSample-out-2-users-10-20am-aug10-2017.csv", "w")
testFile2.write("number of events record,wall clock time,throughput,Avg,Min,Max,Err")
testFile2.write('\n')
with open('/home/gwthamy/Desktop/Task2/jmeter-out-2-users-10-20am-aug10-2017.txt') as f:
    for _ in xrange(4):
        next(f)
    # testFile1 = open(filepath, "r")

    # testFile1Content = f.readlines()
    # print testFile1Content
    str = ""
    counter = 0

    for line in f:

        if "summary = " in line:
            continue
        elif "UTC" in line:
            continue

        line = line.strip()
        # data = line.split("in")[0]
        # str = data.replace("summary +", "")
        # str+=","
        # print str
        data2 = line.strip()
        data2 = line.split("Active")[0]
        if "summary +" and "in" in line:
            str = data2.replace("summary +", "").replace("in", ",").replace("=", ",").replace("/s", "").replace("Avg:",
                                                                                                                 ","
                                                                                                                 "").replace(
                "Min:", ",").replace("M,:", ",").replace("Max:", ",").replace("Err:",
                                                                              ","
                                                                              "")
            # str += ""
            # str+=data2.replace("in","")
        # data = line.split("Active")[1]

        # data3=line.split("
        # Active")[0]
        testFile2.write(str + '\n')
        print str

