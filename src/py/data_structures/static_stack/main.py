from static_stack import *

def main():
    my_stack = StaticStack(capacity=8)
    print(my_stack)
    my_stack.push(10)
    print(my_stack)
    my_stack.push(5)
    print(my_stack)
    my_stack.push(0)
    print(my_stack)
    my_stack.push(100)
    print(my_stack)


if __name__ == "__main__":
    main()