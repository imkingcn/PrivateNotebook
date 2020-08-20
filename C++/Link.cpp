#include"iostream"
using namespace std;
typedef struct LNode{
	int data;
	LNode *Next;
}LNode,*Linklist;
void init(Linklist &L){
	L=new LNode;
	L->Next=NULL;
}
void created(Linklist &L)
{
    Linklist p=L;//新创建一个p指针指向头节点L
    for(int i=0;i<20;i++)//循环创建20个节点的单链表
    {
        Linklist q=new LNode;//创建一个新的节点，并用q指针指向这个新的节点
        q->data=i;//将i的值存入q的data域
        q->Next=NULL;//将q的Next指针指向为空
        p->Next=q;//将q/L的尾指针指向新创建的q这个结构体
        p=q;//再将p指向位置移动到q（p指针后移）
    }
}
void push(Linklist &L)
{
	int n,m;
	Linklist p=L;
	cout<<"输入在第几个后面插入："<<endl;
	cin>>n;
	for (int i = 0; i < n; i++)
	{
		/* code */
		p=p->Next;
	}
	Linklist q=new LNode;
	cout << "输入插入的数值：" << endl;
	cin >> m;
	q->data=m;
	q->Next=p->Next;
	p->Next=q;
}
void deleted(Linklist &L)
{
	int n;
	Linklist p,q;
	p=L;
	cout<<"输入在第几个后面删除："<<endl;
	cin>>n;
	for (int i = 0; i < n; i++)
	{
		/* code */
		p=p->Next;
	}
	q=p->Next;
	p->Next=q->Next;
}
void print(Linklist &L)
{
	Linklist find=L->Next;
	while(find)
	{
		cout<<find->data<<endl;
		find=find->Next;
	}
}
int main()
{
	Linklist L;
	init(L);
	created(L);
	push(L);
	print(L);
	cout<<"======================"<<"\n";
	deleted(L);
	print(L);
}
