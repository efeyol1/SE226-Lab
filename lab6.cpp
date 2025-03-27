#include <iostream>
using namespace std;


double harmonic_recursive(int n) {
    if (n == 1) return 1.0;
    return (1.0 / n) + harmonic_recursive(n - 1);
}


int global_n = 5;

double harmonic_no_param() {
    return harmonic_recursive(global_n);
}

int main() {
    int n;
    cout << "Enter n for harmonic series: ";
    cin >> n;
    cout << "Harmonic series H" << n << " = " << harmonic_recursive(n) << endl;
    
    cout << "Harmonic series using global variable H" << global_n << " = " << harmonic_no_param() << endl;
    
    return 0;
}
