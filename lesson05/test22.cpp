#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
 
struct Student {
    string name, surname;
    double aver;
};
 
bool cmp (Student a, Student b) {
    return a.aver > b.aver;
}
 
int main (void) {
    int n;
    cin >> n;
    if (n < 1) return 1;
 
    vector <Student> data(n);
    for (int i = 0; i < n; ++i) {
        int x,y,z;
        cin >> data[i].name >> data[i].surname;
        cin>>x>>y>>z;
        data[i].aver = (x+y+z)/3.0;
    }
    stable_sort(data.begin(), data.end(), cmp);
 
    for (auto s : data)
        cout << s.name << " " << s.surname << endl;
    return 0;
}