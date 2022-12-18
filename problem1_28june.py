def findpath(arr,list1,i,j):
    if i==m-1 or j==n-1:
        #list1.append(arr[:i][:j])
        print(set(list1))

    else:
        if i+1<m:
            list1.append(arr[i][j])
            findpath(arr,list1,i+1,j)
        
        if j+1<n:
            list1.append(arr[i][j])
            findpath(arr,list1,i,j+1)

        if i+j<m and j+1<n:
            list1.append(arr[i][j])
            findpath(arr,list1,i+1,j+1)

        list1.pop()

m=3
n=3
arr=[[1,2,3],[4,5,6],[7,8,9]]
findpath(arr,[],0,0)