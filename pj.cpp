#include <iostream>
#include <list>
#include <string>

using namespace std;

class Flight {
private:
    int id;
    string start;
    string end;
    int cost;

public:
    void input(int index) {
        cout << "Nhap ma chuyen bay [" << index + 1 << "]: ";
        cin >> id;

        cin.ignore();

        cout << "Nhap dia diem khoi hanh [" << index + 1 << "]: ";
        getline(cin, start);

        cout << "Nhap dia diem den [" << index + 1 << "]: ";
        getline(cin, end);

        cout << "Nhap gia ve [" << index + 1 << "]: ";
        cin >> cost;
    }

    void display() const {
        cout << "MA: " << id
             << ", KHOI HANH: " << start
             << ", DEN: " << end
             << ", GIA: " << cost << endl;
    }

    int getId() const {
        return id;
    }

    int getCost() const {
        return cost;
    }
};

int main() {
    list<Flight> flights;
    int menu;

    do {
        cout << "\n===========================================\n";
        cout << "         MENU CANG HANG KHONG\n";
        cout << "===========================================\n";
        cout << "1. Them Chuyen Bay\n";
        cout << "2. Hien Thi Danh Sach Chuyen Bay\n";
        cout << "3. Tim Kiem Chuyen Bay\n";
        cout << "4. Hien Thi Chuyen Bay co gia ve Cao Nhat\n";
        cout << "5. Hien Thi Chuyen Bay co gia ve Thap Nhat\n";
        cout << "0. Thoat\n";
        cout << "Chon muc tuong ung: ";

        cin >> menu;

        switch (menu) {
        case 1: {
            cout << "------------------\n";
            cout << "Them Chuyen Bay\n";
            cout << "------------------\n";

            Flight fl;
            int index = flights.size();
            fl.input(index);
            flights.push_back(fl);

            cout << "\nDa them chuyen bay.\n";
            break;
        }

        case 2: {
            cout << "\nDanh sach chuyen bay:\n";

            if (flights.empty()) {
                cout << "(Trong)\n";
            } else {
                int index = 1;
                for (const Flight& fl : flights) {
                    cout << "[" << index++ << "] ";
                    fl.display();
                }
            }
            break;
        }

        case 3: {
            cout << "------------------\n";
            cout << "Tim Kiem Chuyen Bay\n";
            cout << "------------------\n";

            if (flights.empty()) {
                cout << "Danh sach trong.\n";
                break;
            }

            int x;
            cout << "\nNhap Ma Chuyen Bay Can tim: ";
            cin >> x;

            bool found = false;

            for (const Flight& st : flights) {
                if (st.getId() == x) {
                    cout << "  Tim thay chuyen bay:\n";
                    st.display();
                    found = true;
                    break;
                }
            }

            if (!found) {
                cout << "Khong tim thay chuyen bay co ma: " << x << "\n";
            }
            break;
        }

        case 4: {
            if (flights.empty()) {
                cout << "Danh sach trong.\n";
                break;
            }

            int maxCost = 0;
            int i = 0;

            for (const Flight& fl : flights) {
                if (i == 0) {
                    maxCost = fl.getCost();
                } else if (fl.getCost() > maxCost) {
                    maxCost = fl.getCost();
                }
                i++;
            }

            cout << "\nCac chuyen bay co gia cao nhat (" << maxCost << "):\n";
            for (const Flight& fl : flights) {
                if (fl.getCost() == maxCost) {
                    fl.display();
                }
            }
            break;
        }

        case 5: {
            if (flights.empty()) {
                cout << "Danh sach trong.\n";
                break;
            }

            int minCost = 0;
            int i = 0;

            for (const Flight& fl : flights) {
                if (i == 0) {
                    minCost = fl.getCost();
                } else if (fl.getCost() < minCost) {
                    minCost = fl.getCost();
                }
                i++;
            }

            cout << "\nCac chuyen bay co gia thap nhat (" << minCost << "):\n";
            for (const Flight& fl : flights) {
                if (fl.getCost() == minCost) {
                    fl.display();
                }
            }
            break;
        }

        case 0:
            cout << "Tam biet!\n";
            break;

        default:
            cout << "Lua chon khong hop le (Nhap 0-5).\n";
            break;
        }

    } while (menu != 0);

    return 0;
}
