def subsequence(a,index,subarray,array):
    if index==len(a):
        if len(subarray)!=0:
            length=len(subarray)
            array.append(sum(subarray)//length)
    else:
        subsequence(a,index+1,subarray,array)

        subsequence(a,index+1,subarray+[a[index]],array)
    return array

n=int(input())
l=list(map(int,input().split()))
a=subsequence(l,0,[],[])
print(max(a))
