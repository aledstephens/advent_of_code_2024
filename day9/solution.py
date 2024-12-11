"""
Part 1 Complete
"""
import time

def is_full_pair(pair):
    """
    Helper function to account for odd numbered disk map
    """

    if len(pair) > 1:
        file_len = int(pair[0])
        space_len = int(pair[1])

    else:
        file_len = int(pair[0])
        space_len = 0

    return file_len, space_len


def convert_input(data: str) -> list:
    """
    Convert from disk map to blocks.
    """

    data = [data[i:i+2] for i in range(0, len(data), 2)] #split data into pairs
    converted_list = []

    for index, pair in enumerate(data): #loop over pairs

        file_len, space_len = is_full_pair(pair)

        for file in range(file_len): #append file index one by one
            converted_list.append(str(index))

        for space in range(space_len): #append spaces one by one
            converted_list.append(".")

    return converted_list


def count_files_in_list(converted_list: list) -> int:
    """
    Helper function to count the number of files in the list, to know how many elements to loop over
    """

    dots_in_list = converted_list.count(".")
    files_in_list = len(converted_list) - dots_in_list
    return files_in_list


def apportion_elements(converted_list: list) -> list:
    """
    Apportion the elements from RHS to LHS spaces.
    Function uses a few versions of the lists to avoid issues with index/length changes during loop:
    Converted list is not modified. Stealing list is shortened. Writing list is lengthened.
    """

    stealing_list = converted_list.copy()
    writing_list =[]

    file_count = count_files_in_list(converted_list)

    for index in range(file_count):

        element = converted_list[index]

        if element == ".":
            if stealing_list[-1] != ".":
                writing_list.append(stealing_list.pop())
            else:
                # remove all dots from the end of the list then use next file
                while stealing_list[-1] == ".":
                    stealing_list.pop()
                writing_list.append(stealing_list.pop())

        else:
            writing_list.append(element)

    return writing_list


def calculate_checksum(apportioned_list):
    """
    Calculate checksum of apportioned list
    """

    checksum = 0
    for index, element in enumerate(apportioned_list):
        checksum += index * int(element)
    return checksum


if __name__ == "__main__":
    file_path = "day9/input_data/input_data.txt"
    data = open(file_path).read().strip()

    start = time.time()

    converted_list = convert_input(data)
    apportioned_list = apportion_elements(converted_list)
    checksum = calculate_checksum(apportioned_list)
    print(f"checksum: {checksum}")

    end = time.time()
    print(f"Time taken: {end - start}")

