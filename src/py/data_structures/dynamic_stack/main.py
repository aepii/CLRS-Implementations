from dynamic_stack import *

def main():
    my_stack = DynamicStack(capacity=4)
    print(my_stack, my_stack._stack)
    my_stack.push(10)
    my_stack.push(10)
    my_stack.push(10)
    my_stack.push(10)
    print(my_stack, my_stack._stack)
    my_stack.push(10)
    print(my_stack, my_stack._stack)
    my_stack.push(10)
    my_stack.push(10)
    my_stack.push(10)
    print(my_stack, my_stack._stack)
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    my_stack.pop()
    print(my_stack, my_stack._stack)
    my_stack.pop()
    my_stack.pop()
    print(my_stack, my_stack._stack)

if __name__ == "__main__":
    main()