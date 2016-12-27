def frequent_words(Text,k):
    Text = Text.strip() #strip()����ȥ��ǰ��Ŀո�
    k = int(k) #int()��ֵ������

    #Generate hastable
    kmer_count = {} #{}�����ֵ��������ͣ��ɼ���ֵ��ɡ�ð�ţ��ֿ�����ֵ�����Ÿ����顣
    for i in range(len(Text) - k):
        c = Text[i:i+k]
        kmer_count[c] = kmer_count[c] + 1 if c in kmer_count else 1 #��ʱ������Hashtable���ֵ���÷�

    max = 0
    max_kmer = []
    for k,v in kmer_count.items():# items��һ�ֵ�����
        if v > max:
            max_kmer = [k]
            max = v
        elif v == max:
            max_kmer += [k]

    print (max_kmer)
