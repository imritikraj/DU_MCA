#include <stack>
#include <iostream>
using namespace std;

class Queue{
    private: 
        stack<int> input;
        stack<int> output;
        
        void transferElement(){
            while(!input.empty()){
            output.push(input.top());
            input.pop();
            }
        }
    
    public: 
        void enqueue(int num){
            input.push(num);
        }
        int dequeue(){
            if(empty()){
                throw runtime_error("Queue is empty");
            }
            if(output.empty()){
                transferElement();
            }
            int front = output.top();
            output.pop();
            return front;
        }
        int peek(){
            if (empty()) {
            throw runtime_error("Queue is empty");
            }
            
            if (output.empty()) {
                transferElement();
            }
            
            return output.top();
        }
        bool empty(){
            return input.empty()  && output.empty();
        }
        int size(){
            return input.size() + output.size();
        }
};





int main(){
    Queue q;
    q.enqueue(0);
    q.enqueue(2);
    cout << q.peek();
    q.dequeue();
    q.enqueue(6);
    q.enqueue(1);
    cout << q.peek();
    q.dequeue();
    cout << q.peek();
    return 0;
}











