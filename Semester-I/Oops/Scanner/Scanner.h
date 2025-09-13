#ifndef SCANNER_H
#define SCANNER_H

// --- Standard Library Includes ---
#include <iostream>   // For input/output operations (std::cin, std::cout)
#include <string>     // For using the std::string class
#include <limits>     // For std::numeric_limits, used in input validation

// --- Function Declarations and Definitions ---

/**
 * @brief Reads a value of a specified type from standard input.
 *
 * This template function provides a safe way to get user input. It handles
 * invalid input by clearing the error state and prompting the user again
 * until a valid value of the specified type (T) is entered.
 *
 * @tparam T The data type of the value to be read (e.g., int, double, string).
 * @return The valid value entered by the user.
 */
template <typename T>
T input() {
    T value;
    // Loop until a valid value is successfully read
    while (!(std::cin >> value)) {
        std::cout << "Invalid input. Please enter a valid value." << std::endl;
        std::cin.clear(); // Clear the error flag on the input stream
        // Discard all characters in the input buffer up to the newline
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
    return value;
}

/**
 * @brief Prints a value to standard output without a newline.
 *
 * This template function can print any data type to the console.
 * It does not append a newline character, so subsequent output will
 * appear on the same line.
 *
 * @tparam T The data type of the value to be printed.
 * @param value The value to print.
 */
template <typename T>
void print(T value) {
    std::cout << value;
}

/**
 * @brief Prints a value to standard output followed by a newline.
 *
 * This template function is a convenience wrapper that prints any data type
 * and then moves the cursor to the next line.
 *
 * @tparam T The data type of the value to be printed.
 * @param value The value to print.
 */
template <typename T>
void println(T value) {
    std::cout << value << std::endl;
}

/**
 * @brief Reads an integer from standard input.
 * @return The integer value entered by the user.
 */
int nextInt() {
    return input<int>();
}

/**
 * @brief Reads a double-precision floating-point number from standard input.
 * @return The double value entered by the user.
 */
double nextDouble() {
    return input<double>();
}

/**
 * @brief Reads a single word (non-whitespace string) from standard input.
 * @return The string entered by the user.
 */
std::string nextStr() {
    return input<std::string>();
}

/**
 * @brief Reads an entire line of text from standard input, including spaces.
 * @return The line of text entered by the user.
 */
std::string nextLine() {
    std::string line;
    std::getline(std::cin, line);
    return line;
}

#endif // SCANNER_H