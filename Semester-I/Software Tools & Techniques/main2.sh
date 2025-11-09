#!/bin/bash

# This script creates and sets up the main script with proper filename

# Sample data for demonstration
NAME="John Doe"
ROLL="1234"

# Get first 4 letters (lowercase, padded)
first_four=$(echo "$NAME" | head -c 4 | tr '[:upper:]' '[:lower:]')
length=${#first_four}

while [ $length -lt 4 ]; do
    first_four="${first_four}_"
    length=$((length + 1))
done

filename="${first_four}_${ROLL}.sh"

echo "Creating script: $filename"

# Create the script file
cat > "$filename" << 'EOF'
#!/bin/bash

# Function to validate roll number
validate_roll() {
    local roll=$1
    if [[ ! "$roll" =~ ^[0-9]+$ ]]; then
        echo "ERROR: Roll number must be numeric" >&2
        exit 2
    fi
}

# Function to get first 4 letters of name (lowercase, padded with underscores)
get_first_four() {
    local name=$1
    local first_four=$(echo "$name" | head -c 4 | tr '[:upper:]' '[:lower:]')
    local length=${#first_four}
    
    # Pad with underscores if less than 4 characters
    while [ $length -lt 4 ]; do
        first_four="${first_four}_"
        length=$((length + 1))
    done
    
    echo "$first_four"
}

# Main script logic

# Get name and roll from positional arguments or prompt if not provided
NAME=$1
ROLL=$2

# If name not provided, prompt for it
if [ -z "$NAME" ]; then
    read -p "Enter name: " NAME
fi

# If roll not provided, prompt for it  
if [ -z "$ROLL" ]; then
    read -p "Enter roll number: " ROLL
fi

# Trim whitespace from name
NAME=$(echo "$NAME" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')

# Validate roll number
validate_roll "$ROLL"

# Print the required output
echo "Student: $NAME"
echo "Roll: $ROLL"
EOF

# Make the script executable
chmod +x "$filename"

echo "Script created and made executable: $filename"