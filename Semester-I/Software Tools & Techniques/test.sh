#!/bin/bash

# Test script for the assignment

echo "=== Testing the script ==="
echo

# Test 1: Using positional arguments
echo "Test 1: Using positional arguments"
./john_1234.sh "John Doe" "1234"
echo

# Test 2: Interactive mode (no arguments)
echo "Test 2: Interactive mode"
echo -e "Jane Smith\n5678" | ./john_1234.sh
echo

# Test 3: Invalid roll number
echo "Test 3: Invalid roll number"
./john_1234.sh "John Doe" "abc123"
echo

# Test 4: Name with less than 4 characters
echo "Test 4: Short name example"
./bo__100.sh "Bo Li" "100"
echo