#include <queue>
#include <iostream>
using namespace std;

class Stack
{
private:
    queue<int> q1, q2;
    void transferElement()
    {
        while (q1.size() > 1)
        {
            q2.push(q1.front());
            q1.pop();
        }
    }

public:
    void push(int x)
    {
        q1.push(x);
    }

    int pop()
    {
        if (empty())
        {
            throw runtime_error("Stack is empty");
        }

        transferElement();

        int top = q1.front();
        q1.pop();

        // Swap q1 and q2
        swap(q1, q2);

        return top;
    }

    int top()
    {
        if (empty())
        {
            throw runtime_error("Stack is empty");
        }

        transferElement();

        int topElement = q1.front();
        q2.push(topElement);
        q1.pop();

        swap(q1, q2);

        return topElement;
    }

    bool empty()
    {
        return q1.empty();
    }

    int size()
    {
        return q1.size();
    }
};

int main()
{
    Stack s;
    s.push(0);
    s.push(1);
    cout << s.top();
    s.pop();
    cout << s.top();

    return 0;
}