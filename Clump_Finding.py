#网上抄的代码，以后再来慢慢看
from collections import defaultdict

def clumps_finding(k, L, t):
    data = open("d:\sample.txt")
    inseq = data.read()
    inseq = str(inseq)
    lookup = defaultdict(list)
    clump = set()

    for cursor in range(len(inseq) - k + 1):
        seg = inseq[cursor:cursor + k]

        # remove prior positions of the same segment
        # if they are more than L distance far
        while lookup[seg] and cursor + k - lookup[seg][0] > L:
            lookup[seg].pop(0)

        lookup[seg].append(cursor)
        if len(lookup[seg]) == t:
            clump.add(seg)
    
    #clump是一个set,区别于list的是无序排列并且没有重复值。输出到txt需要将每个元素字符化并且换行。
    r = open("d:\esult.txt","w")
    for i in clump:
        k="".join([str(j)for j in i])
        r.write(k+"\n")
    r.close()
    print(len(clump))#找出有多少个clumps
