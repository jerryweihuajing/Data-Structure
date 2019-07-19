#include <iostream>

//定义数组类
class CArray {

	//amount of elment
	int size;

	//指向动态分配的数组
	int* pointer;
public:
	//声明构造函数,s为数组元素个数
	CArray(int s = 0);

	//重载构造函数
	CArray(CArray& a);

	//声明析构函数
	~CArray();

	//在尾部添加一个元素v
	void push_back(int v);

	//用于数组对象间的赋值
	CArray& operator=(const CArray& a);

	//返回数组元素的个数
	int length();

	//用于支持a[i]=3这样的赋值语句
	int& operator[](int i);
};

//构造函数:s为数组元素个数
CArray::CArray(int s) {

	if (s == 0)
		pointer = NULL;

	else
		pointer = new int[s];
}

//构造函数:a为CArray对象
CArray::CArray(CArray & a) {
	if (a.pointer == NULL) {
		pointer = NULL;
		size = 0;
		return;
	}
	pointer = new int[a.size];
	memcpy(pointer, a.pointer, sizeof(int) * a.size);
	size = a.size;
}

//析构函数
CArray::~CArray() {
	if (pointer != NULL)
		delete[]pointer;
}

//赋值号使得左右两边的对象内容相同
CArray& CArray::operator=(const CArray & a)
{
	//防止a=a这样的错误
	if (pointer == a.pointer)
		return *this;

	//如果a的数组是空的
	if (a.pointer == NULL) {

		//释放空间
		if (pointer != NULL)
			delete[]pointer;
		pointer = NULL;
		size = 0;
		return *this;
	}

	//如果原有空间足够大就不用分配新空间
	//如果不够大，需要分配新空间
	if (size < a.size) {
		if (pointer != NULL)
			delete[]pointer;
		pointer = new int[a.size];
	}
	memcpy(pointer, a.pointer, sizeof(int) * a.size);
	size = a.size;
	return*this;
}

//在数组尾部添加一个元素
void CArray::push_back(int v) {
	if (pointer != NULL) {

		//重新分配空间
		int* tmpPointer = new int[size + 1];

		//拷贝原数组
		memcpy(tmpPointer, pointer, sizeof(int) * size);

		delete pointer;
		pointer = tmpPointer;
	}
	if (pointer == NULL) {
		pointer = new int[1];
	}

	//加入新的元素,等价于pointer[size]=v;size=size+1;
	pointer[size++] = v;

	//std::cout << v;
}

//返回数组的长度
int CArray::length() {
	return size;
}

//重载运算符[]
int& CArray::operator[](int i) {
	return pointer[i];
}

int main()
{
	//编写可变长数组
	CArray a;//开始数组是空的
	for (int i = 0; i < 5; i++) {
		a.push_back(i);
		//std::cout << i;
	}

	CArray a2, a3;
	a2 = a;
	for (int i=0; i < a.length(); ++i) {
		std::cout << a2[i] << " ";
	}

	a2 = a3;//a2 is void
	std::cout << std::endl;
	a[3] = 100;
	CArray a4(a);

	for (int i = 0; i < a4.length(); ++i) {
		std::cout << a4[i] << " ";
	}
	//std::cout << "Hello World!\n";
}
