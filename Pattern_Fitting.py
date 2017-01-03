def pattern_fitting(text):
    data = open("d:\sample.txt")
    seq = data.read()
    seq = str(seq)
    print (seq)
    print (text)
    k = len(text)
    n = len(seq)
    kmers = []
    for i in range(0, n-k+1): 
        kmers.append(seq[i:i+k])#借用kmers取值，首字母刚好是原seq的编号
        if kmers[i]==text: #从list里面取元素，使用编号i就行
            b=i   #这一步把i转换
            print (b)
