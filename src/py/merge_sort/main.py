from merge_sort import *

def main():
    my_array = [5, 2, 4, 6, 1, 3]
    print(f"Before Insertion Sort: {my_array}")
    merge_sort(my_array, 0, len(my_array)-1)
    print(f"After Insertion Sort: {my_array}")

if __name__ == "__main__":
    main()