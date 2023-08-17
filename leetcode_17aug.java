class Pair{
    int first,second,third;
    Pair(int first,int second,int third){
        this.first=first;
        this.second=second;
        this.third=third;
    }
}
class Solution {
    int direction[][]={{-1,0},{1,0},{0,-1},{0,1}};
    public int[][] updateMatrix(int[][] mat) {
        Queue<Pair> queue=new LinkedList<>();
        int m=mat.length;
        int n=mat[0].length;
        int ans[][]=new int[m][n];
        int vis[][]=new int[m][n];
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(mat[i][j]==0)
                {
                    vis[i][j]=1;
                    queue.add(new Pair(i,j,0));
                }
            }
        }
        while(!queue.isEmpty()){
            int len=queue.size();
            for(int i=0;i<len;i++)
            {
                int row=queue.peek().first;
                int col=queue.peek().second;
                int dis=queue.peek().third;
                queue.poll();
                ans[row][col]=dis;
                for(int j=0;j<4;j++)
                {
                    int nrow=row+direction[j][0];
                    int ncol=col+direction[j][1];
                    if(nrow>=0 && nrow<m && ncol>=0 && ncol<n && vis[nrow][ncol]==0 && mat[nrow][ncol]==1)
                    {
                        queue.add(new Pair(nrow,ncol,dis+1));
                        vis[nrow][ncol]=1;
                    }
                }
            }
        }
        return ans;
    }
}
