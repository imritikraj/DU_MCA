#include <iostream>
using namespace std;
/*
*🔑 Common Operations on a Singly Linked List
1. Insertion

At the beginning (insertAtStart) ✅ (you already did this)

At the end (insertAtEnd) ✅ (you did this too)

At a given position (index-based)

2. Deletion

Delete by value ✅ (you did this)

Delete at a given position

Delete the entire list (free all nodes)

3. Searching

Search for a value (return true/false or the index if found)

4. Traversal

Print list ✅ (done)

Print in reverse (recursive or by stack)

5. Utility operations

Count the number of nodes (length of list)

Find the middle element

Find N-th node from the end

Detect a loop (Floyd’s Cycle Detection)

Reverse the linked list (iterative & recursive)

Merge two sorted linked lists

Remove duplicates (if sorted list)

6. Advanced variations

Rotate the list (left/right by k nodes)

Partition the list around a value (like quicksort partitioning)

Check if the list is a palindrome

Flatten a list (if it has multiple levels)
*/
struct Node {
    int data;
    Node* next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

void display(Node *head) {
    Node *temp = head;
    while (temp != NULL) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

void insertAtHead(Node*& head, int x) {
    Node *temp = new Node(x);
    temp->next = head;
    head = temp;
}

void insertAtTail(Node*& head, int x) {
    Node *temp = new Node(x);
    if (head == NULL) {
        head = temp;
        return;
    }
    Node *last = head;
    while (last->next != NULL) {
        last = last->next;
    }
    last->next = temp;
}

int main() {
    Node *head = NULL;
    insertAtHead(head, 10);
    insertAtHead(head, 20);
    insertAtHead(head, 30);
    display(head);      // prints: 30 20 10
    insertAtTail(head, 40);
    display(head);      // prints: 30 20 10 40
    return 0;
}
