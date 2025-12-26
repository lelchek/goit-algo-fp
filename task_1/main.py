import random
from linked_list import LinkedList
from reverse import reverse_list
from merge_sort import merge_sort


def main():
    l_list = LinkedList()

    values = random.sample(range(1, 101), 20)
    for value in values:
        l_list.insert_at_beginning(value)

    print("\n--------- ORIGINAL LIST ---------")
    l_list.print_list()

    l_list.head = reverse_list(l_list.head)
    print("\n--------- REVERSED LIST ---------")
    l_list.print_list()

    l_list.head = merge_sort(l_list.head)
    print("\n--------- SORTED LIST ---------")
    l_list.print_list()


if __name__ == "__main__":
    main()
