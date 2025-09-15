#include <iostream>
#include <iomanip>
#include <queue>
using namespace std;

int sum = 0;
struct  TreeNode{
    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

// Print tree level by level (vertical structure)
void printTreeV(TreeNode* root) {

    if (!root) return;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int size = q.size();  // nodes at current level

        // Print all nodes at this level
        for (int i = 0; i < size; i++) {
            TreeNode* node = q.front();
            q.pop();

            cout << node->data << " ";

            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        cout << endl; // new line after each level
    }
}


// Function to print tree in "tree shape"
void printTreeH(TreeNode* root, int space = 0, int gap = 5) {
    if (root == NULL) return;

    // Increase distance between levels
    space += gap;

    // Print right child first (so tree is horizontal)
    printTreeH(root->right, space);

    // Print current node after spaces
    cout << endl;
    for (int i = gap; i < space; i++)
        cout << " ";
    cout << root->data << "\n";

    // Print left child
    printTreeH(root->left, space);
}


void inorderTraversal(TreeNode* root) {
    if (root == NULL) {
        return;
    }
    sum = sum + root->data;
    inorderTraversal(root->left);
    cout << root->data << " ";
    inorderTraversal(root->right);
}

void postorderTraversal(TreeNode* root) {
    if (root == NULL) {
        return;
    }

    postorderTraversal(root->left);
    postorderTraversal(root->right);
    cout << root->data << " ";
}

void preorderTraversal(TreeNode* root) {
    if (root == NULL) {
        return;
    }
    cout << root->data << " ";
    preorderTraversal(root->left);
    preorderTraversal(root->right);
}

int main() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);

    // In-order traversal: 4 2 5 1 6 3 7
    // Pre-order traversal: 1 2 4 5 3 6 7
    // Post-order traversal: 4 5 2 6 7 3 1
    // printTreeV(root);
    // cout << "In-order traversal: ";
    inorderTraversal(root);

    cout << "sum = " <<sum << endl;
    return 0;
}