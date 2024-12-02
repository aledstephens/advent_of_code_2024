'''
Day 2:
Including the damper by dropping each element and storing each check as a pass/fail
'''

def import_data():
    file_path = 'day2/input_data/input_data.txt'
    with open(file_path, 'r') as file:
        data = [[int(num) for num in line.split()] for line in file]
    return data


def check_magnitude_of_difference(difference):
    if (difference == 0) or (abs(difference) > 3):
        # print(f'Difference is not compliant, report is not safe, skipping...')
        return False
    else:
        return True


def check_increasing_or_decreasing(signs):
    if all(signs) or not any(signs):
        return True
    else:
        return False


def check_distance_store(difference_store):
    if all(difference_store):
        return True
    else:
        return False


def check_safe_report(difference_store, signs_store):
    if check_distance_store(difference_store) & check_increasing_or_decreasing(signs_store):
        return True
    else:
        return False


def check_report(report):

    signs_store = [] # store the positive/negative differences
    difference_store = [] # store whether differences are out of bounds

    # loop through the single report
    for index, element in enumerate(report):

        # only store last_element at report start
        if index == 0:
            last_element = element

        else:
            difference = element - last_element # otherwise store the difference

            difference_store.append(check_magnitude_of_difference(difference))
            signs_store.append(True if difference > 0 else False) # store if difference is positive / negative

            last_element = element # update last_element

    safe_report = check_safe_report(difference_store, signs_store)

    return safe_report


def count_safe_reports_with_damper(input):
    print(f'No of reports: {len(input)}')
    safe_report_count = 0

    for report in input:
        report_result = []

        # loop through the report, dropping each element in turn
        for i in range(len(report)):
            temp_report = report[:i] + report[i + 1:]

            # check the report is safe each time and record in list
            report_result.append(check_report(temp_report))

        # mark as safe if any are safe
        if any(report_result):
            safe_report_count += 1

    return safe_report_count


if __name__ == "__main__":
    input = import_data()
    result = count_safe_reports_with_damper(input)
    print(f'Safe reports: {result}')
