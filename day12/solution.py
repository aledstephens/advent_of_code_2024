"""
Day 12: Part 1

Method:
- Load the data into a numpy array

- Group crops
    - Go through the array finding region by region
    - Store locations under plant type and region group no

- Calculate perimeter
    - For each group define the boundaries by combining each location with its neighbours
    - Drop duplicated boundaries
    - Calculate running total of region size * perimeter length
"""

import numpy as np

def load_data(file_path: str) -> np.array:
    input = np.loadtxt(file_path, dtype=str, comments=None)
    char_list = [list(line) for line in input] # split the lists into individual characters
    array = np.array(char_list)
    print(f"Loaded array size: {array.shape}")

    return array


def calculate_neighbour_positions(position: tuple) -> list:
    i, j = position[0], position[1]

    return [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]


def validate_positions(positions, limit=4):

    return [position for position in positions if 0 <= position[0] <= limit and 0 <= position[1] <= limit]


def drop_searched_positions(positions, already_searched):

    return [position for position in positions if position not in already_searched]


def init_crop_group_count(crops):
    crop_group_count = {}

    for value in np.unique(crops):
        crop_group_count[value] = 0

    return crop_group_count


def group_crops(crops):
    print(f"Grouping crops...")
    grid_limit = crops.shape[0] - 1

    already_searched = []
    plant_store = {}
    crop_group_count = init_crop_group_count(crops)

    for coord, value in np.ndenumerate(crops):

        if coord in already_searched: #ignore already searched locations
            continue

        print(f"Processing coord: {coord}, crop: {value}")
        group = crop_group_count[value] #set group number
        crop_group_count[value] += 1

        if value not in plant_store: #add the group to the plant store
            plant_store[value] = {}
        plant_store[value][group] = [coord]

        already_searched.append(coord) #mark as searched location

        search_list = [coord] #set up list to search through

        while search_list: #keep searching until the list is empty
            next_search = search_list.pop()
            neighbours = calculate_neighbour_positions(next_search)
            neighbours = validate_positions(neighbours, grid_limit)
            neighbours = drop_searched_positions(neighbours, already_searched)

            for neighbour in neighbours:
                if crops[neighbour] == value:
                    search_list.append(neighbour)  # add to the list of neighbours to search
                    plant_store[value][group].append(neighbour)
                    already_searched.append(neighbour)

    return plant_store


def calculate_perimeter(plant_store):
    print(f"Calculating perimeter...")
    running_total = 0

    for key, value in plant_store.items():
        for group, locations in value.items():


            plant_count = len(locations)
            print(f"Processing group {group}, of crop {key}, size {plant_count}")
            boundaries = []

            for location in locations:
                # find neighbours
                neighbours = calculate_neighbour_positions(location)

                for neighbour in neighbours:
                    boundary = [location, neighbour] # create a boundary definition
                    boundaries.append(boundary)

            # find unique boundaries
            sorted_boundaries = []

            for boundary in boundaries:
                sorted_boundaries.append(tuple(sorted(boundary)))

            unique_boundaries = set(sorted_boundaries)
            dropped_count = len(sorted_boundaries) - len(unique_boundaries)

            unique_boundary_count = len(unique_boundaries) - dropped_count # account for duplicates

            running_total += plant_count * unique_boundary_count

    return running_total


if __name__ == "__main__":
    crops = load_data("day12/input_data/input_full.txt")
    plant_store = group_crops(crops)
    total = calculate_perimeter(plant_store)
    print(f"Total price of fencing all regions: {total}")
