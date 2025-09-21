#include <iostream>
#include <vector>
#include <thread>
#include <chrono>
using namespace std;

// function to print pegs with disks
void printPegs(vector<int> A, vector<int> B, vector<int> C) {
    cout << "\n--- Current State ---\n";
    cout << "A: ";
    for (int d : A) cout << d << " ";
    cout << "\nB: ";
    for (int d : B) cout << d << " ";
    cout << "\nC: ";
    for (int d : C) cout << d << " ";
    cout << "\n---------------------\n";
}

// recursive tower of hanoi with visualization
void towerOfHanoi(int n, vector<int>& source, vector<int>& dest, vector<int>& aux,
                  char sName, char dName, char aName) {
    if (n == 0) return;

    // move n-1 disks from source → auxiliary
    towerOfHanoi(n - 1, source, aux, dest, sName, aName, dName);

    // move the nth disk (last one) from source → destination
    int disk = source.back();
    source.pop_back();
    dest.push_back(disk);

    // print the move
    this_thread::sleep_for(chrono::seconds(1)); // wait 1 second
    cout << "Move disk " << disk << " from " << sName << " to " << dName << endl;

    // show state of all pegs
    printPegs(source, aux, dest);

    // move n-1 disks from auxiliary → destination
    towerOfHanoi(n - 1, aux, dest, source, aName, dName, sName);
}

int main() {
    int n;
    cout << "Enter number of disks: ";
    cin >> n;

    // initialize pegs
    vector<int> A, B, C;
    for (int i = n; i >= 1; i--) {
        A.push_back(i); // larger numbers = larger disks
    }

    // initial state
    printPegs(A, B, C);

    // solve Tower of Hanoi
    towerOfHanoi(n, A, C, B, 'A', 'C', 'B');

    return 0;
}
