testFile2 = open("/home/gwthamy/Desktop/Task 3/extract-2-01pm.csv", "w")
testFile2.write("Time-stamp-of-record,Average latency (ms),Average throughput (events/second)"+"\n")
def extractData(filepath):
    testFile1 = open(filepath, "r")
    testFile1Content = testFile1.readlines()
    # print testFile1Content
    str = "";
    counter = 0;
    for line in testFile1Content:
        if "user admin connected" in line:
            continue
        line = line.strip()
        data = line.split(",")[0]

        if counter % 3 == 0:

            str = data.replace("[", "")
            str += ","
        elif counter % 3 == 1:
            str += data.replace("Event: avgLatency:", "")
            str += ","
        elif counter % 3 == 2:
            str += data.replace("throughput:", "")
            #str += ","

        if counter != 0 and counter % 3 == 2:
            testFile2.write (str + "\n")

        counter += 1

extractData("/home/gwthamy/Desktop/Task 3/extract-2-01pm.txt")
