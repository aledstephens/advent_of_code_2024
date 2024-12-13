"""
Day 11 - Part 1 & Part 2
Trick to get part 2 to run efficiently was to use a map to record count of each stone,
rather than holding value of each stone individually.

Rules:
# rule 1 - find 0s and make 1
# rule 2 - split even digits
# rule 3 - multiply by 2024
"""

def split_even_numbers(stone, no_digits):
    first_part = str(stone)[:(int(no_digits / 2))]
    second_part = str(stone)[int((no_digits / 2)):]
    return int(first_part), int(second_part)


def add_to_map(stone, count, final_map):
    if stone in final_map:
        final_map[stone] += count
    else:
        final_map[stone] = count

    return final_map


def create_map_from_list(arrangement):
    map = {}

    for item in arrangement:
        if item in map:
            map[item] += 1
        else:
            map[item] = 1

    return map


def run_algorithm(initial_arrangement, total_blinks):

    initial_map = create_map_from_list(initial_arrangement) # create map of stone value and count

    for blink in range(1, total_blinks + 1):
        print(f"blink no. {blink} of {total_blinks}")

        final_map = {}

        for key, value in initial_map.items():
            stone = key
            count = value
            # print(f"stone: {stone}, count: {count}")

            if stone == 0:
                # print(f"there are {count} stone value {stone}. making them 1s")
                final_map = add_to_map(1, count, final_map)
                continue

            no_digits = len(str(stone))

            if no_digits % 2 == 0:
                first_part, second_part = split_even_numbers(stone, no_digits)
                # print(f"there are {count} stone value {stone}. They have even numbers. Making first part: {first_part} & second part: {second_part}")
                final_map = add_to_map(first_part, count, final_map)
                final_map = add_to_map(second_part, count, final_map)

            else:
                # print(f"There are {count} stone value {stone}. Is 'other' value so multiplying by 2024")
                stone *= 2024
                final_map = add_to_map(stone, count, final_map)

        print(f"Blink {blink}, final stone values: {len(final_map)}, total stones: {sum(final_map.values())}")
        # replace arrangement
        initial_map = final_map

    return final_map


if __name__ == "__main__":

    initial_arrangement = [890, 0, 1, 935698, 68001, 3441397, 7221, 27]
    total_blinks = 75

    result = run_algorithm(initial_arrangement, total_blinks)

    total_stones = sum(result.values())
    print(f"Total stones: {total_stones}")