#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    
    Node(int val) {
        data = val;
        next = nullptr;
    }
};

class Stack {
private:
    Node* head;     // Points to top element of stack.
    int num;        // Number of elements (index-style tracking).
    int capacity;   // Fixed size limit (resized when full).

public:
    Stack(int initialCapacity) {  // You can set any initial size.
        head = nullptr;
        num = 0;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num >= capacity) {
            increaseCapacity();
        }
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        num++;
    }

    int pop() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        int topValue = head->data;
        Node* temp = head;
        head = head->next;
        delete temp;
        num--;
        return topValue;
    }

    int peek() {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return num <= 0;
    }

    void increaseCapacity() {
        capacity *= 2;
        cout << "Stack capacity increased to: " << capacity << endl;
    }

    bool deleteElement(int val) {
        if (isEmpty()) {
            cout << "Stack is empty!" << endl;
            return false;
        }

        Node* temp = head;
        Node* prev = nullptr;

        while (temp != nullptr) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    head = temp->next;
                } else {
                    prev->next = temp->next;
                }
                delete temp;
                num--;
                return true;
            }
            prev = temp;
            temp = temp->next;
        }
        cout << "Element not found in stack." << endl;
        return false;
    }
};

int main() {
    Stack myStack(3);
    myStack.push(5);
    myStack.push(10);
    myStack.push(15);
    
    cout << "Top element: " << myStack.peek() << endl;
    
    myStack.push(20); // Should trigger increaseCapacity()
    
    cout << "Popped: " << myStack.pop() << endl;
    cout << "Popped: " << myStack.pop() << endl;
    
    myStack.deleteElement(10);
    
    return 0;
}
