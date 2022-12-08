#include <iostream>
using namespace std;

class Node{
           public:
           char name[20];
           char prn[10];
           Node *Next;
};

class SLL{
    public:
    Node *create(){
    Node *N;
    N = new Node();
    cout << "Enter name:";
    cin >> N -> name;
    cout << "Enter prn:";
    cin >> N -> prn;
    N -> Next = NULL;
  return  N;
}

void display(Node *N) {
  Node* ptr;
   cout << N->name << "" ;
   cout << N->prn << "" ;
}
};

Node* insert(Node *N)
{
Node *c, *NN;
c = N;
NN = new Node();
cout << N->name << "";
cout << N->prn << "";
cin >> NN -> name;
cin >> NN -> prn;
NN->Next = NULL;
{
while(c->Next!=NULL)
c = c->Next;
c->Next = NN;
return N;
}
};

void Display(Node *N){
while(N!=NULL)
{
cout << N -> name << "";
cout << N->prn << "";
N = N->Next;
}
};

int main() {
SLL l1;
Node *N;
N = l1.create();
l1.display(N);
}
