"""
Day 11 - Part 1
# rule 1 - find 0s and make 1
# rule 2 - split even digits
# rule 3 - multiply by 2024
"""



def split_even_numbers(stone, no_digits):
    first_part = str(stone)[:(int(no_digits / 2))]
    second_part = str(stone)[int((no_digits / 2)):]
    return int(first_part), int(second_part)

def run_algorithm(initial_arrangement, total_blinks):

    for blink in range(1, total_blinks + 1):
        print(f"blink no. {blink} of {total_blinks}")

        final_arrangement = []

        for stone in initial_arrangement:

            if stone == 0:
                # print(f"stone: {stone} is 1. making it zero")
                final_arrangement.extend([1])
                continue

            no_digits = len(str(stone))

            if no_digits % 2 == 0:
                first_part, second_part = split_even_numbers(stone, no_digits)
                # print(f"stone: {stone} has even numbers. first part: {first_part}, second part: {second_part}")
                final_arrangement.extend([first_part, second_part])

            else:
                # print(f"stone: {stone} is not one and has odd numbers. multiplying by 2024")
                final_arrangement.extend([stone * 2024])

        print(f"Blink {blink}, final stones: {len(final_arrangement)}")
        # replace arrangement
        initial_arrangement = final_arrangement

    return final_arrangement

if __name__ == "__main__":

    initial_arrangement = [890, 0, 1, 935698, 68001, 3441397, 7221, 27]
    total_blinks = 25 #simply changing to 75 for part 2 will take a looooong time.

    result = run_algorithm(initial_arrangement, total_blinks)
    print(len(result))







