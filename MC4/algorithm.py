import pandas as pd 
import numpy as np
import time
from MC4.utility import is_valid_path, get_filename
import os

np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})


def get_dataframe(file_name):

    return pd.read_csv(file_name, header=0, index_col=0)


def get_matrix_shape(df):

    rows = len(df.index)
    cols = len(df.columns)

    return rows, cols


def get_partial_transition_matrix(df, rows, cols):

    resultant_matrix = list()

    for i in range(rows):
        for j in range(rows):
            
            # print(f'\ni = {i}, j = {j}')
            result = len(df.columns[df.iloc[i] < df.iloc[j]])
            # print(result)

            if result == 0 and i==j:
                val = -1
            elif result >= (cols/2):
                val = 0
            else:
                val = 1

            matrix_input = val

            resultant_matrix.append(val)

    return np.array(resultant_matrix).reshape(rows, rows)


def get_normalized_transition_matrix(matrix, rows):

    matrix = matrix / rows

    for i in range(rows):
        for j in range(rows):
            if i == j:

                result1 = sum(matrix[i, i+1:rows])
                result2 = sum(matrix[i, 0:j])
                result = result1 + result2
                
                matrix[i,j] = 1 - result

    return matrix


def get_ergodic_transition_matrix(normalized_transition_matrix, rows):

   return (normalized_transition_matrix * 0.85) + (0.15/rows)


def get_initial_state_matrix(rows):

    return np.repeat((1/rows), rows)


def get_stationary_matrix(state_matrix, transition_matrix, precision, iterations):

    counter = 1

    # print('\nStationary matrix calculation...')

    while counter <= iterations:

        current_state_matrix = state_matrix

        new_state_matrix = state_matrix.dot(transition_matrix)

        error = new_state_matrix - current_state_matrix

        if (np.abs(error) < precision).all():
            break

        # print(f'iter: {counter} | Matrix: {state_matrix} | error: {error}')

        # time.sleep(0.3)

        state_matrix = new_state_matrix

        counter += 1
    
    return state_matrix


def calculate_aggregated_ranks(matrix):

    a = {}
    rank = 1
    
    for num in sorted(matrix, reverse = True):
        if num not in a:
            a[num] = rank
            rank = rank+1

    final_ranks = [a[i] for i in matrix]

    return final_ranks


# def display_ranks(index, final_ranks):

#     print('\nContestantwise ranks...\n')

#     for index_val, rank in zip(index, final_ranks):
#         print(f'{index_val} : {rank}', end = ' | ')

#     print()


def MC4_Aggregator(file_path, header=0, index_col=0, precision=0.0000001, iterations=200):

    if is_valid_path(file_path):

        file_name = get_filename(file_path)

        df = get_dataframe(file_name)
        # print(df)
        rows, cols = get_matrix_shape(df)
        partial_transition_matrix = get_partial_transition_matrix(df, rows, cols)
        # print(partial_transition_matrix)
        normalized_transition_matrix = get_normalized_transition_matrix(partial_transition_matrix, rows)
        # print(normalized_transition_matrix)
        ergodic_transition_matrix = get_ergodic_transition_matrix(normalized_transition_matrix, rows)
        # print(ergodic_transition_matrix)
        initial_state_matrix = get_initial_state_matrix(rows)
        # print(initial_state_matrix)
        stationary_matrix = get_stationary_matrix(initial_state_matrix, ergodic_transition_matrix, precision, iterations)
        # print(stationary_matrix)
        final_ranks = calculate_aggregated_ranks(stationary_matrix)
        
        return final_ranks

