from insertion_sort import *

def main():
    my_array = [5, 2, 4, 6, 1, 3]
    print(f"Before Insertion Sort: {my_array}")
    insertion_sort(my_array)
    print(f"After Insertion Sort: {my_array}")

    my_array_2 = [5, 2, 4, 6, 1, 3]
    print(f"Before Insertion Sort: {my_array_2}")
    insertion_sort(my_array_2, ascending=False)
    print(f"After Insertion Sort: {my_array_2}")

if __name__ == "__main__":
    main()