def frequent_words(Text,k):
    Text = Text.strip() #strip()可以去掉前后的空格
    k = int(k) #int()将值整数化

    #Generate hastable
    kmer_count = {} #{}代表字典数据类型，由键对值组成。冒号：分开键和值，逗号隔开组。
    for i in range(len(Text) - k):
        c = Text[i:i+k]
        kmer_count[c] = kmer_count[c] + 1 if c in kmer_count else 1 #暂时不明白Hashtable和字典的用法

    max = 0
    max_kmer = []
    for k,v in kmer_count.items():# items是一种迭代器
        if v > max:
            max_kmer = [k]
            max = v
        elif v == max:
            max_kmer += [k]

    print (max_kmer)
