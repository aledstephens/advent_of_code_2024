'''
Day 2:
Solved by looping through each element in a report.
If a difference between 2 elements is out of bounds it skips to the next report.
If the differences are ok, it checks the signs are all positive or negative.
I'm also tracking which reports are safe to plot the distribution.
'''

def import_data():
    file_path = 'day2/input_data/input_data1.txt'
    with open(file_path, 'r') as file:
        data = [[int(num) for num in line.split()] for line in file]
    return data


def check_magnitude_of_difference(difference):
    if (difference == 0) or (abs(difference) > 3):
        # print(f'Difference is not compliant, report is not safe, skipping...')
        return True
    else:
        return False


def check_increasing_or_decreasing(signs):
    if all(signs) or not any(signs):
        safe_report = 1
    else:
        safe_report = 0
    return safe_report


def count_safe_reports(input):
    print(f'No of reports: {len(input)}')
    safe_reports = 0
    report_tracker = []

    for report in input: # loop through each report

        signs = [] # store the positive/negative differences
        report_not_safe = False # flag to break out of loop

        elements = len(report)

        # loop through a single report
        for index, element in enumerate(report):

            # only store last_element at report start
            if index == 0:
                last_element = element

            else:
                difference = element - last_element # otherwise store the difference

                report_not_safe = check_magnitude_of_difference(difference)

                if report_not_safe:
                    break # break to the next report

                signs.append(True if difference > 0 else False) # store if difference is positive / negative

                last_element = element # update last_element

        if report_not_safe:
            report_tracker.append(0)
            continue

        report_tracker.append(1)

        safe_reports += check_increasing_or_decreasing(signs)

    return safe_reports, report_tracker

if __name__ == "__main__":
    input = import_data()
    result, report_tracker = count_safe_reports(input)
    print(f'Safe reports: {result}')

    # noticed that safe reports are not random
    import plotly.express as px
    fig = px.bar(
        x = [i for i in range(1, len(report_tracker)+1)],
        y = report_tracker,
    )
    # update x and y axis labels
    fig.update_xaxes(title_text='Report No')
    fig.update_yaxes(title_text='Safe Report (1 = Safe)')
    fig.show()