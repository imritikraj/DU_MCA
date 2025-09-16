#include <iostream>
using namespace std;


struct TreeNode{
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};


void swapNode(TreeNode* root) {
    if (root == NULL) return;

    // swap child pointers
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;

    // recurse for children
    swapNode(root->left);
    swapNode(root->right);
}


int main(){
    return 0;
}