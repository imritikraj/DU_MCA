#include <iostream>
using namespace std;
/**
 * Computes the greatest common divisor (GCD) of two integers
 * This function recursively applies the principle that the GCD of two numbers does not change 
 * if the larger number is replaced by its remainder when divided by the smaller number.
 * The recursive relation used is: gcd(a, b) = gcd(b % a, a).
 * 'a' The first integer. it acts as the divisor.
 * 'b' The second integer. it acts as the dividend.
 * return The greatest common divisor of integers a and b.
 */
int gcd(int a, int b) {
    // Base Case: If 'a' divides 'b' evenly, then 'a' is the greatest common divisor.
    if (b % a == 0) {
        return a;
    }
    
    // Recursive Step: The problem is reduced by applying the Euclidean algorithm property.
    // The next iteration will find the GCD of the current divisor ('a') and the remainder ('b % a').
    int remainder = b % a;
    return gcd(remainder, a);
}


int main() {
    // Define two numbers to find their GCD.
    int num1 = 10;
    int num2 = 50;
    
    // Call the gcd function and print the result in a descriptive way.
    // Note---> The order of parameters doesn't matter for the algorithm's correctness.
    
    
    // gcd(86, 70) will lead to a recursive call of gcd(70, 86), which then proceeds normally.
    cout << "The GCD of " << num1 << " and " << num2 << " is: " << gcd(num1, num2) << endl;
    
    return 0;
}