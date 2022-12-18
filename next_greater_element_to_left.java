class Sol{
    public long void ngel(){
        long ans[]=new long[n];
        Stack<Long> stack=new Stack<>();
        for(int i=0;i<n;i++)
        {
            long curr=arr[i];
            while(stack.size() != 0 && stack.peek() <= curr)
                stack.pop();
                
            if(stack.size() == 0)
                ans[i]=-1;
                
            else{
                ans[i]=stack.peek();
            }
            stack.push(curr);
        }
        return ans;
    }
    public static void main(){
    }
}
    