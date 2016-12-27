# 第一次用biophython！

def rev(Text): 

    from Bio.Seq import Seq
    reverse = Seq(Text) 
    print (reverse.reverse_complement())
