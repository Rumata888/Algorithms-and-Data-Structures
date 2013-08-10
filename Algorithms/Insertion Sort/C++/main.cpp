#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

class InsertionSort
{
public:
	void SortArr(int* arr,int n);
};

void InsertionSort::SortArr(int* arr,int n)
	{
		int a;
		int k;
		for (int i=1;i<n;i++)
		{
			a=arr[i];
			k=i-1;
			while((k>=0)&&(arr[k]>a))
			{
				arr[k+1]=arr[k];
				k--;
			}
			arr[k+1]=a;

		}

}

int main()
{
	int* arr =new int[3]{3,2,1};
	InsertionSort sh;
	cout <<"shit"<<endl;
	sh.SortArr(arr,3);
	cout <<arr[0]<<"::"<<arr[1]<<"::"<<arr[2]<<endl;
	return 0;

}
