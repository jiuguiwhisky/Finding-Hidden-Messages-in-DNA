#Target: Count the specifical patterns in DNA reads
#Input: A string Text and the pattern
#Output: Count(Text,pattern)

#Algorithm example provide by textbook
#PatternCount(Text, Pattern)
        #count ← 0
        #for i ← 0 to |Text| − |Pattern|
            #if Text(i, |Pattern|) = Pattern #第i项，值为|Pattern|也就是k
                #count ← count + 1

        #return count

def kmers(Text, pattern):
    count=0 
    pattern_len=len(pattern)
    for i in range(len(Text)):
		    if Text[i:i+pattern_len]== pattern: #==判断是否相等
			      count +=1 #count加1，python中+=表示加值为1

    print (count)
