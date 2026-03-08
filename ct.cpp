#include <iostream>
#include <list>
#include <string>
#include <limits>

using namespace std;

class Employee {
private:
    int roll;
    int salary;

public:
    void input(int index) {
        cout << "Enter Roll of Employee [" << index + 1 << "]: ";
        cin >> roll;
        cout << "Enter Salary of Employee [" << index + 1 << "]: ";
        cin >> salary;
    }
    void display() const {
        cout << "Roll No: " << roll << " Salary: " << salary << endl;
    }

    int getSalary() const {
        return salary;
    }

    int getRoll() const {
        return roll;
    }
};

int main() {
    list<Employee> employees;
    int numEmployees;

    do {
        cout << "Enter the number of employees: ";
        if (!(cin >> numEmployees)) {
            cout << "Invalid input. Please enter a non-negative integer.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            numEmployees = -1;
            continue;
        }
        if (numEmployees < 0) {
            cout << "Please enter 0 or a positive number.\n";
        }
    } while (numEmployees < 0);
    
    if (numEmployees == 0) {
        cout << "No employees entered. Exiting program.\n";
        return 0;
    }

    for (int i = 0; i < numEmployees; i++) {
        Employee emp;
        while (true) {
            emp.input(i);
            if (!cin.fail()) break;
            cout << "Invalid input detected. Please re-enter this employee.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }
        employees.push_back(emp);
    }

    int choice;

    do {
        cout << "\nMenu:\n";
        cout << "1. Display all employees\n";
        cout << "2. Show employees with the highest salary\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        if (!(cin >> choice)) {
            cout << "Invalid choice. Please enter a number.\n";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            choice = 0;
        }

        switch (choice) {
        case 1:
            cout << "\nEmployee Data:\n";
            if (employees.empty()) { cout << "(none)\n"; break; }
            {
                int index = 1;
                for (list<Employee>::iterator it = employees.begin(); it != employees.end(); ++it) {
                    cout << "[" << index++ << "] "; 
                    it->display();
                }
            }
            break;

        case 2: 
            {
                if (employees.empty()) {
                    cout << "No employees available.\n";
                    break;
                }

                int maxSalary = employees.begin()->getSalary();
                for (list<Employee>::const_iterator it = employees.begin(); it != employees.end(); ++it) {
                    if (it->getSalary() > maxSalary) {
                        maxSalary = it->getSalary();
                    }
                }

                cout << "\nEmployees with the highest salary (" << maxSalary << "):\n";
                for (list<Employee>::const_iterator it = employees.begin(); it != employees.end(); ++it) {
                    if (it->getSalary() == maxSalary) {
                        it->display();
                    }
                }
            }
            break;

        case 3: 
            cout << "Exiting program.\n";
            break;

        default:
            cout << "Invalid choice! Please try again.\n";
        }

    } while (choice != 3);

    return 0;
}