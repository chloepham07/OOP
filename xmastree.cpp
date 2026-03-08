#include <iostream>
#include <cstdlib>
#include<unistd.h>
#include<ctime>
using namespace std;
void drawtree(int n);
int main(){
  int n;
  srand(time(0));
  cout<<"input n ";
  cin>>n;
  drawtree(n);  
  int lines= n+ n/3 +3;
  while(true){
    usleep(40000);
    cout << "\033[" << lines << "A";
    drawtree(n);
  }
  return 0;
}

void drawtree(int n){
  //cout << "\033[2J\033[1;1H";
  for (int i = 1; i <= n; i++){
    for (int j = 1; j <= n - i; j++){
      cout << " ";
    }
    for (int j = 1; j <= i; j++){
      int color = rand() % 10;
      if(color == 1) cout << "\e[0;32m";
      else if(color == 2) cout << "\e[0;33m";
      else if(color == 3) cout << "\e[0;36m";
      else if(color == 4) cout << "\e[0;37m";
      else if(color == 5) cout << "\e[38;5;195m";
      else if(color == 6) cout << "\e[38;5;159m";
      else if(color == 7) cout << "\e[38;5;196m";
      else if(color == 8) cout << "\e[38;5;220m";
      else if(color == 9) cout << "\e[38;5;214m";
      else cout << "\e[0;31m";
      cout << "* ";
    }
    cout << "\n";
  }
  int trunk = n / 3;
  for(int i = 0; i < trunk; i++){
    for(int j = 0; j < n - 2; j++){
      cout << " ";
    }
    cout << "\033[0m" << "|||" << "\033[0m" << endl;
  }
  cout << endl << "   \033[33m★\033[0m Merry Christmas!\n" << endl;
}