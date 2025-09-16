#include <iostream>
using namespace std;


/**
 * computes the greatest common divisor (GCD) of two integers
 * This function recursively applies the principle that the GCD of two numbers does not change 
 * if the larger number is replaced by its remainder when divided by the smaller number.
 * The recursive relation used is: gcd(a, b) = gcd(b % a, a).
 * 'a' The first integer. it acts as the divisor.
 * 'b' The second integer. it acts as the dividend.
 * return The greatest common divisor of integers a and b.
 */
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
/**
 * Computes the least common multiple (LCM) of two integers
 * This function first computes the greatest common divisor (GCD) of the two numbers
 * using the Euclidean algorithm. It then uses the formula: lcm(a, b) = (a * b) / gcd(a, b)
 * to compute the LCM. The division is performed first to avoid overflow.
 * 'a' The first integer.
 * 'b' The second integer.
 * return The least common multiple of integers a and b.
 */

int lcm(int a, int b) {
    return (a / gcd(a, b)) * b;  // divide first to avoid overflow
}

int main() {
    cout << lcm(4, 6);  // Output: 12
    return 0;
}
