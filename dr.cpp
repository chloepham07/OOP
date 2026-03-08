#include <iostream>
#include <list>
using namespace std;
class Employee{
    private:
    int rollno;
    int salary;
    public:
    void input(int index){
        cout << "enter roll of employee [" << index+1 << "]: ";
        cin >> rollno;
        cout << "enter salary of employee [" << index+1 << "]: ";
        cin >> salary;
    }
    void display()const{
        cout << "roll no: " << rollno << " salary: " << salary << '\n';
    }
    int getsalary() const {
        return salary;
    }
    int getroll() const{
        return rollno;
    }
};
int main(){
   list<Employee> employees;
   int numemployee = 0;
   cout << "How many employees? ";
   if (!(cin >> numemployee) || numemployee <= 0) {
       cerr << "Invalid number of employees\n";
       return 1;
   }
   for (int i = 0; i < numemployee; ++i){
    
    Employee emp;
    emp.input(i);
    employees.push_back(emp);
   }
   cout << "\nEmployee data:\n";
   int index = 1;
   for (const Employee &employee : employees) {
       cout << index++ << ". ";
       employee.display();
   }
   return 0;
   int choice;
   do{
    cout<<"\nMenu\n";
    cout<<"1. Display all enployees\n";
    cout<<"2. Show employee with the highest salary\n";
    cout<<"3. Exit";
    switch(choice){
        case 1:
    }
   }while(choice !=3);
}
