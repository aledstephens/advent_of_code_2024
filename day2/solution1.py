'''
Day 2:
Solved by looping through each element in a report.
Records if the difference between 2 elements is out of bounds.
Records if the differences are all positive or negative.
I'm also tracking which reports are safe to plot the distribution.
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


def count_safe_reports(input):
    print(f'No of reports: {len(input)}')
    safe_reports = 0
    report_tracker = []

    for report in input: # loop through each report

        signs_store = [] # store the positive/negative differences
        difference_store = [] # store whether differences are out of bounds

        elements = len(report)

        # loop through a single report
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

        if safe_report:
            report_tracker.append(True)
            safe_reports += 1

        else:
            report_tracker.append(False)

    return safe_reports, report_tracker

if __name__ == "__main__":
    input = import_data()
    result, report_tracker = count_safe_reports(input)
    print(f'Safe reports: {result}')

    # # noticed that safe reports are not random
    # import plotly.express as px
    # fig = px.bar(
    #     x = [i for i in range(1, len(report_tracker)+1)],
    #     y = report_tracker,
    # )
    # # update x and y axis labels
    # fig.update_xaxes(title_text='Report No')
    # fig.update_yaxes(title_text='Safe Report (1 = Safe)')
    # fig.show()