# import rules

def load_input(file_path: str) -> list:

    with open(file_path) as f:
        data = f.read().splitlines()

    return data



def check_validity(rules: list, updates: list, fix_update: bool = False) -> dict:
    validity_map = {}

    for update in updates:
        # print(f'Update is: {update}')
        valid_update = True

        for rule in rules:
            rule = rule.split("|")
            fore = rule[0]
            aft = rule[1]

            # skip if fore or aft not in update
            if fore not in update:
                # print("fore page not in this update")
                continue

            if aft not in update:
                # print("aft page not in this update")
                continue

            # get index of first occurrence of fore and aft in update
            fore_index = update.find(fore)
            # print(f'found fore at index: {fore_index}')
            aft_index = update.find(aft)
            # print(f'found aft at index: {aft_index}')

            # check if fore comes before aft
            if fore_index > aft_index:

                if fix_update:
                    print(f'Fixing update: {update} by swapping {fore} and {aft}')
                    # swap fore and aft
                    update = update.replace(fore, "temp")
                    update = update.replace(aft, fore)
                    update = update.replace("temp", aft)

                else:
                    valid_update = False

        # update validity map
        if valid_update:
            validity_map[update] = True
        else:
            validity_map[update] = False

    return validity_map


def sum_mid_pages(validity_map: dict) -> int:
    # get true keys from validity map
    valid_updates = [key for key in validity_map if validity_map[key] == True]
    valid_updates_count = len(valid_updates)
    invalid_updates = [key for key in validity_map if validity_map[key] == False]

    page_sum = 0

    for update in valid_updates:
        lst = update.split(",")
        mid_page = lst[int(len(lst)/2)]
        page_sum += int(mid_page)

    return page_sum, valid_updates_count, invalid_updates


if __name__ == "__main__":

    rules = load_input("day5/input_data/rules-test.txt")
    updates = load_input("day5/input_data/updates-test.txt")

    #Part 1
    print(f'No of updates: {len(updates)}')
    validity_map = check_validity(rules, updates, fix_update=False)
    result, valid_count, invalid_updates = sum_mid_pages(validity_map)
    print(f'No of valid updates: {valid_count}')
    print(f'Sum of mid pages: {result}')

    #Part 2 - not correct
    fixed_map = check_validity(rules, invalid_updates, fix_update=True)
    result, valid_count, invalid_updates = sum_mid_pages(fixed_map)
    print(f'No of fixed updates: {valid_count}')
    print(f'Sum of mid pages: {result}')