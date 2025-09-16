
#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;

    TreeNode(int val){
        data = val;
        left = NULL;
        right = NULL;
    }
};

TreeNode* insertBST(TreeNode* root, int val) {
    if (root == NULL) {
        return new TreeNode(val);
    }
    if (val < root->data) {
        root->left = insertBST(root->left, val);
    } else {
        root->right = insertBST(root->right, val);
    }
    return root;
}

TreeNode* createTree(vector<int> v) {
    TreeNode* root = NULL;
    for (int val : v) {
        root = insertBST(root, val);
    }
    return root;
}


int main(){
    vector<int> v = {1, 2, 3, 4, 5, 6, 7};
    createTree(v);
    return 0;
}