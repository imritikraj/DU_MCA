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


int maxNode(TreeNode* root){
    if(root == NULL){
        return 0;
    }
    return max(root->data, max(maxNode(root->left), maxNode(root->right)));
}


int main(){
    return 0;
}