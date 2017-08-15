testFile2 = open("/home/gwthamy/Desktop/Task 3/2-01pm.csv", "w")
testFile2.write("time since start (s),sent events,time to send (ms),throughput events,entire experiment throughput")
testFile2.write('\n')
with open("/home/gwthamy/Desktop/Task 3/2-01pm.txt") as f:
    for _ in xrange(19):
        next(f)

    str = " "

    for line in f:
        line = line.strip()
        data = line.split(":")[1]
        str = data.replace("Sent", ",").replace("sensor events in", ",").replace(
            "milliseconds with total throughput of",
            ",").replace("events/second",
                         "").replace(".","").replace("Entire "
                                     "experiment throughput", ",")
        data2 = line.split(":")[2]
        str+=data2
        print str
        testFile2.write(str+'\n')

