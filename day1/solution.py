import numpy as np
import pandas as pd
from collections import Counter

# load input data
def load_data():
    '''
    Required manually saving 2 csv files which doesn't seem ideal.
    '''
    df1 = pd.read_csv('day1/input_data/list1.csv', header=None)
    df2 = pd.read_csv('day1/input_data/list2.csv', header=None)
    list1 = df1[0].tolist()
    list2 = df2[0].tolist()
    return list1, list2

def compute_distance(list1, list2):
    list1.sort()
    list2.sort()
    distance = abs(np.subtract(list1, list2))
    total = np.sum(distance)
    return total

def similarity_score(list1, list2):
    '''
    After much faffing with numpy and pandas,
    I discovered the Counter class in the collections module,
    it made the solution much tidier.
    '''
    counts = Counter(list2)

    total = 0

    for element in list1:
        if element in counts:
            total += element * counts[element]
    return total


if __name__ == "__main__":
    list1, list2 = load_data()
    result1 = compute_distance(list1, list2)
    print(f'distance total: {result1}')
    result2 = similarity_score(list1, list2)
    print(f'similarity score: {result2}')



