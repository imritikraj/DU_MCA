#include <iostream>
using namespace std;

// Correct Node structure with a template type
template <typename T>
struct Node {
    T val;
    Node* next;
    Node* pre;
    
    // Correct constructor
    Node(T v) {
        val = v;
        next = nullptr;
        pre = nullptr;
    }
};

// Insert a new node at a specific position
// The head is a pointer to a pointer to allow modification of the original head
template <typename T>
void insert(Node<T>** head, T val, int pos = -1) {
    // 1. Create the new node
    Node<T>* newNode = new Node<T>(val);

    // 2. Handle empty list insertion (first node)
    if (*head == nullptr) {
        *head = newNode;
        return;
    }

    // 3. Insertion at the beginning (pos == 0)
    if (pos == 0) {
        newNode->next = *head;
        (*head)->pre = newNode;
        *head = newNode;
        return;
    }
    
    // 4. Insertion at the end or middle
    Node<T>* temp = *head;
    
    // Insertion at the end (pos == -1)
    if (pos == -1) {
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->pre = temp;
    } 
    // Insertion at a specific position
    else {
        int count = 0;
        // Traverse to the node *before* the insertion point
        while (temp->next != nullptr && count < pos - 1) {
            temp = temp->next;
            count++;
        }
        // Handle invalid position
        if (count != pos - 1 && temp->next != nullptr) {
            cout << "Position out of bounds. Appending to tail." << endl;
            // Fallback to tail insertion
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
            newNode->pre = temp;
            return;
        }

        newNode->next = temp->next;
        if (temp->next != nullptr) {
            temp->next->pre = newNode;
        }
        temp->next = newNode;
        newNode->pre = temp;
    }
}

// Function to display the list
template <typename T>
void display(Node<T>* head) {
    Node<T>* temp = head;
    while (temp != nullptr) {
        cout << temp->val << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    Node<int>* head = nullptr;
    
    insert(&head, 1, 0); // Insert 1 at the beginning
    display(head);
    
    insert(&head, 5, -1); // Insert 5 at the end
    display(head);
    
    insert(&head, 3, 1); // Insert 3 in the middle
    display(head);
    
    return 0;
}