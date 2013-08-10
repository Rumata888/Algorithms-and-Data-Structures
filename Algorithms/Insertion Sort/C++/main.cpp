#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

class FileUsage{
public:
	static int* LoadArrayFromFile(char* filename,int& n);
	static void SaveArrayToFile(char* filename,int* array, int n);
};
class CLIInput{};
class InsertionSort
{
public:
	void SortArr(int* arr,int n);
};

int* FileUsage::LoadArrayFromFile(char* filename, int& n)
{
	string line;
	ifstream myfile(filename);
	int* array;
	int i=0;
	if(myfile.is_open()){
		getline(myfile,line);
		n=atoi(line.c_str());
		array=new int[n];
		while(myfile.good())
		{
			getline(myfile,line);
			array[i]=atoi(line.c_str());
			i++;
		}
		myfile.close();
		return array;
	}
	else
	{
		cout<<"Could not open file";
		return 0;
	}

}
void FileUsage::SaveArrayToFile(char* filename,int* array, int n)
{
	string line;
	ofstream myfile(filename);
	int i;
	if(myfile.is_open()){
		myfile<<n<<endl;;
		for(i=0;i<n;i++)
		{
			myfile<<array[i]<<endl;
		}
		myfile.close();
		delete[] array;
	}
	else
	{
		cout<<"Could not open file";
	}

}

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
	char g;
	char filename[100];
	int* array;
	int n;
	cout<<"Take from file(1) or simple input(2)? Anything else to quit"<<endl;
	cin>>g;
	if (g=='1')
	{
		cout<<"Enter file name: ";
		cin>>filename;
		array=FileUsage::LoadArrayFromFile(filename,n);
	}
	else
	{
		return 0;
	}

	InsertionSort sh;
	sh.SortArr(array,n);
	if(g=='1')
	{
		FileUsage::SaveArrayToFile("output.txt",array,n);
	}
	return 0;

}
