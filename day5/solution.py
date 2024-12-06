'''
Part 1 is a validity check
Part 2 is a fixes the updates by running each one through the rules backwards and forwards until all rules pass.
'''

def load_input(file_path: str) -> list:
    with open(file_path) as f:
        data = f.read().splitlines()

    return data


def get_fore_aft(rule: str) -> tuple:
    rule = rule.split("|")
    return rule[0], rule[1]


def move_aft(update: list, fore_index: int, aft: str) -> list:
    update.remove(aft)
    update.insert(fore_index, aft)

    return update


def check_validity(rules: list, updates: list) -> dict:
    validity_map = {}

    for update in updates:
        update = update.split(",") # convert to list
        valid_update = True

        for rule in rules:

            fore, aft = get_fore_aft(rule)

            if fore not in update or aft not in update:
                continue

            # get index of first occurrence of fore and aft in update and check order
            fore_index = update.index(fore)
            aft_index = update.index(aft)

            if fore_index > aft_index:
                valid_update = False

        update = ",".join(update) # convert back to string

        if valid_update:
            validity_map[update] = True
        else:
            validity_map[update] = False

    return validity_map


def get_invalid_updates(validity_map: dict) -> list:
    return [key for key in validity_map if validity_map[key] == False]


def fix_updates(rules: list, updates: list) -> dict:
    """
    To fix, keep running the update through the rules backwards and forwards until it's valid.
    """
    fixed_updates_map = {}

    for update in updates:

        update = update.split(",")

        invalid_update = True

        while invalid_update:

            invalid_rules_count = 0
            rules = rules[::-1] # reverse rules

            for rule in rules:

                fore, aft = get_fore_aft(rule)

                if fore not in update or aft not in update:
                    continue

                fore_index = update.index(fore)
                aft_index = update.index(aft)

                if fore_index > aft_index:
                    invalid_rules_count += 1
                    update = move_aft(update, fore_index, aft) # try fix
                    continue

            if invalid_rules_count == 0:
                invalid_update = False

        # convert update back to string
        update = ",".join(update)

        fixed_updates_map[update] = True

    return fixed_updates_map


def sum_mid_pages(validity_map: dict) -> tuple:
    valid_updates = [key for key in validity_map if validity_map[key] == True]
    valid_updates_count = len(valid_updates)

    page_sum = 0

    for update in valid_updates:
        lst = update.split(",")
        mid_page = lst[int(len(lst)/2)]
        page_sum += int(mid_page)

    return page_sum, valid_updates_count


if __name__ == "__main__":
    #Load data
    rules = load_input("day5/input_data/rules-full.txt")
    updates = load_input("day5/input_data/updates-full.txt")

    #Part 1
    print(f'PART 1: No of updates: {len(updates)}')
    validity_map = check_validity(rules, updates)
    result, valid_count = sum_mid_pages(validity_map)
    print(f'No of valid updates: {valid_count}. Sum of mid pages: {result}') # 143 / 5762

    #Part 2
    invalid_updates = get_invalid_updates(validity_map)
    print(f'PART 2: No of invalid updates: {len(invalid_updates)}')
    fixed_updates_map = fix_updates(rules, invalid_updates)
    result, valid_count = sum_mid_pages(check_validity(rules, fixed_updates_map))
    print(f'After fixing, sum of mid pages: {result}') # 123 / 4130

