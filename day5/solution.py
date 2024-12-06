# import rules

def load_input(file_path: str) -> list:

    with open(file_path) as f:
        data = f.read().splitlines()

    return data


def get_fore_aft(rule: str) -> tuple:
    rule = rule.split("|")
    return rule[0], rule[1]


def move_aft(update: list, fore_index: int, aft: str) -> list:
    # print(f'Reordering update: {update} by moving {aft} before {fore}')
    update.remove(aft)
    update.insert(fore_index, aft)
    return update

def check_validity(rules: list, updates: list) -> dict:
    validity_map = {}

    for update in updates:
        update = update.split(",")
        valid_update = True

        for rule in rules:

            fore, aft = get_fore_aft(rule)

            if fore not in update or aft not in update:
                continue

            # get index of first occurrence of fore and aft in update
            fore_index = update.index(fore)
            aft_index = update.index(aft)

            # check if fore comes before aft
            if fore_index > aft_index:
                valid_update = False

        # convert update back to string
        update = ",".join(update)

        # update validity map
        if valid_update:
            validity_map[update] = True
        else:
            validity_map[update] = False

    return validity_map

def fix_update(rules: list, update: list) -> dict:
    """
    To fix, keep running the update through the rules backwards and forwards until it's valid.
    """

    # print(f'Fixing update: {update}')
    update = update.split(",")

    invalid = True

    while invalid:

        invalid_count = 0
        rules = rules[::-1] # reverse rules

        for rule in rules:

            fore, aft = get_fore_aft(rule)

            if fore not in update or aft not in update:
                continue

            fore_index = update.index(fore)
            aft_index = update.index(aft)
            # print(f'found fore at index: {fore_index}. found aft at index: {aft_index}')

            if fore_index > aft_index:
                invalid_count += 1
                update = move_aft(update, fore_index, aft) # try fix
                continue

        if invalid_count == 0:
            invalid = False


    # convert update back to string
    update = ",".join(update)

    return update


def sum_mid_pages(validity_map: dict) -> int:
    # get true keys from validity map
    valid_updates = [key for key in validity_map if validity_map[key] == True]
    valid_updates_count = len(valid_updates)

    page_sum = 0

    for update in valid_updates:
        lst = update.split(",")
        mid_page = lst[int(len(lst)/2)]
        page_sum += int(mid_page)

    return page_sum, valid_updates_count


if __name__ == "__main__":

    rules = load_input("day5/input_data/rules-full.txt")
    updates = load_input("day5/input_data/updates-full.txt")

    #Part 1
    print('PART 1')
    print(f'No of updates: {len(updates)}')
    validity_map = check_validity(rules, updates)
    result, valid_count = sum_mid_pages(validity_map)
    print(f'No of valid updates: {valid_count}')
    print(f'Sum of mid pages: {result}') # 143 / 5762

    #Part 2
    print('PART 2')
    invalid_updates = [key for key in validity_map if validity_map[key] == False]
    print(f'No of invalid updates: {len(invalid_updates)}')

    fixed_updates_map = {}
    for index, update in enumerate(invalid_updates):
        print(f'Fixing update {index+1} of {len(invalid_updates)}: {update}')
        fixed_updates_map[fix_update(rules, update)] = True

    result, valid_count = sum_mid_pages(check_validity(rules, fixed_updates_map))
    print(f'No of valid updates: {valid_count}')
    print(f'Sum of mid pages: {result}') # 123 / 4130

