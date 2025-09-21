#include <iostream>
using namespace std;

void towerOfHanoi(int n, char source, char destination, char auxiliary) {
    if (n == 0) {
        return; // no disk to move
    }

    // Step 1: move n-1 disks from source → auxiliary
    towerOfHanoi(n - 1, source, auxiliary, destination);

    // Step 2: move the nth (largest) disk from source → destination
    cout << "Move disk " << n << " from " << source << " to " << destination << endl;

    // Step 3: move n-1 disks from auxiliary → destination
    towerOfHanoi(n - 1, auxiliary, destination, source);
}

int main() {
    int n;
    cout << "Enter number of disks: ";
    cin >> n;

    towerOfHanoi(n, 'A', 'C', 'B'); // A = source, C = destination, B = auxiliary
    return 0;
}
