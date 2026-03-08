# include <iostream>
# include <list>
# include <string>
using namespace std;
class Flight{
    private:
        int id;
        int cost;
        string from;
        string to;
    public:
        void input(int index){
            cout<<"Flight["<< index+1<<"]'s ID: ";
            cin>>id;
            cin.ignore();

            cout<<"From: ";
            getline(cin,from);

            cout<<"To: ";
            getline(cin,to);

            cout<<"Ticket price: ";
            cin>>cost;
        };
        void display() const {
            cout<<"Flight["<< index+1<<"]'s ID: "<<id
                <<",From: "<<from
                <<",To "<<to
                <<",Ticket price: "<<cost;
        };
        int getId() const{
            return id;
        };
        int getCost() const{
            return cost;
        };
    };
    int main(){
        list<Flight> flights;
        int menu;
        do{
        cout << "\n===========================================\n";
        cout << "         AIRPORT'S MENU\n";
        cout << "===========================================\n";
        cout << "1. Add a flight\n";
        cout << "2. Show flights list\n";
        cout << "3. Find a flight\n";
        cout << "4. Display Flights with the Highest Prices\n";
        cout << "5. Display Flights with the Lowest Prices\n";
        cout << "0. Exit\n";
        cout << "Select a : ";
        cin >> menu;

        switch(menu){
            case 1: {
            cout << "------------------\n";
            cout << "Add a flight\n";
            cout << "------------------\n";
            Flight fl;
            int index = flights.size();
            fl.input(index);
            flights.push_back(fl);
            break;
            };

            case 2: {
                if(flights.empty()) {
                    cout<<"Empty";
                }
                else {
                int index =1;
                for (const Flight&fl : flights){
                    cout<<"["<<index++ <<"]";
                    fl.display();
                    break;
                }
            };
            }
        }
        }
    }

