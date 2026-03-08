#include <iostream>
#include <list>
using namespace std;
class Student{
  private:
  int ID, score;
  public:
  void input(int index){
    cout<<"enter student's ID: ";
    cin>>ID;
    cout<<"enter student's score: ";
    cin>>score;
  };
  void display(){
    cout<<"ID: "<<ID<<" score: "<<score<<endl;
  }
};
int main(){
  list <Student> student;
  int numstudent;
  cout<<"nhap so hoc sinh: ";
  cin>>numstudent;
  for(int i=0;i<numstudent;i++){
    Student st;
    st.input(i);
    student.push_back(st);
}
cout<<"\nStudents list\n";
int index =1;
for(Student&st:student){
  cout<<index++<<".";
  st.display();
}

}