#include<stdio.h>
#include<math.h>
randomize_part(int a[],int p,int r)
{
	int i,t;
	i=rand(p,r);
	t=a[i];
	a[i]=a[r];
	a[r]=t;
	return partition(a,p,r);
}
partition(int a[],int p,int r)
{
	int x,i,t,j;
	x=a[r];
	i=p-1;
	for(j=p;j<=r-1;j++)
	{
		if(a[j]<=x)
		{
			i=i+1;
			t=a[i];
			a[i]=a[j];
			a[j]=t;
		}
	}
	t=a[i+1];
	a[i+1]=a[r];
	a[r]=t;
	return (i+1);
}
quicksort(int a[],int p,int r)
{
	int q;
	if(p<r)
	{
		q=randomize_part(a,p,r);
		quicksort(a,p,q-1);
		quicksort(a,q+1,r);
	}
}
int main()
{
	int n,i;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	quicksort(a,0,n-1);
	for(i=0;i<n;i++)
	printf("%d ",a[i]);
}
