def find_kmers(Text, k):

    kmers = [] #python中[]代表创建一个空的list
    n = len(Text) #len取string的长度，返回整数
    for i in range(0, n-k+1): #从0取到n-k+1
        kmers.append(Text[i:i+k]) #append是往list里面添加后面括号元素的方法
    return kmers #返回的是一个列表
