def file_write(fname,tasks):
    with open(fname,"w") as fp:
        for x in tasks:
            fp.write("%s\n" % x)
def file_read(fname):
    tasks=[]
    with open(fname,"r") as fp:
        lines=fp.readlines()
        for line in lines:
            tasks.append(line.strip("\n"))
    return tasks