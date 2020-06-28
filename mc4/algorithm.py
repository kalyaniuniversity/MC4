import pandas as pd 
import numpy as np
import time
from mc4.utility import is_valid_path, get_filename
import os

np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})


def get_dataframe(file_path, header_row, index_col):

    """Returns a dataframe object of a csv file

    Args:
        file_path (string): path of the csv file

    Returns:
        pandas.core.Dataframe: pandas dataframe object 
    """

    return pd.read_csv(file_path, header=header_row, index_col=index_col)


def get_matrix_shape(df):

    """Returns shape(rows,cols) of a dataframe

    Args:
        df (pandas.core.Dataframe): pandas dataframe objects

    Returns:
        int,int: shape in the form of rows,cols
    """

    rows = len(df.index)
    cols = len(df.columns)

    return rows, cols


def get_partial_transition_matrix(df, items, lists):

    """Returns the partial transition matrix from the dataframe containing different ranks

    Args:
        df (pandas.core.DataFrame): dataframe object containing different ranks
        items (int): number of items
        lists (int): number of lists

    Returns:
        numpy.ndarray: partial transition matrix
    """

    resultant_matrix = list()

    for i in range(items):
        for j in range(items):
            
            result = len(df.columns[df.iloc[i] < df.iloc[j]])

            if result == 0 and i==j:
                val = -1
            elif result >= (lists/2):
                val = 0
            else:
                val = 1

            matrix_input = val

            resultant_matrix.append(val)

    return np.array(resultant_matrix).reshape(items, items)


def get_normalized_transition_matrix(p_matrix, items):

    """Returns the normalized transition matrix from the partial transition matrix

    Args:
        p_matrix (numpy.ndarray): partial transition matrix
        items (int): number of items

    Returns:
        numpy.ndarray: normalized transition matrix
    """

    p_matrix = p_matrix / items

    for i in range(items):
        for j in range(items):
            if i == j:

                result1 = sum(p_matrix[i, i+1:items])
                result2 = sum(p_matrix[i, 0:j])
                result = result1 + result2
                
                p_matrix[i,j] = 1 - result

    return p_matrix


def get_ergodic_transition_matrix(n_matrix, items, erg_number):

    """Returns the ergotic transition matrix from normalized transition matrix

    Args:
        n_matrix (numpy.ndarray): normalized transition matrix
        items (int): number of items
        erg_number (float): small, positive ergotic number

    Returns:
        numpy.ndarray: ergodic transition matrix
    """
    
    return (n_matrix * (1-erg_number)) + (erg_number/items)


def get_initial_distribution_matrix(items):

    """Returns initial distribution matrix

    Args:
        items (int): number of items

    Returns:
        numpy.ndarray: initial distribution matrix
    """

    return np.repeat((1/items), items)


def get_stationary_distribution_matrix(state_matrix, transition_matrix, precision, iterations):

    """Returns stationary distribution matrix

    Args:
        state_matrix (numpy.ndarray): initial distribution matrix
        transition_matrix (numpy.ndarray): final transition matrix or ergodic transition matrix
        precision (float): acceptable error margin for convergence, default is 1e-07
        iterations (int): number of iterations to reach stationary distribution, default is 200

    Returns:
        numpy.ndarray: stationary distribution matrix
    """

    counter = 1

    while counter <= iterations:

        current_state_matrix = state_matrix

        new_state_matrix = state_matrix.dot(transition_matrix)

        error = new_state_matrix - current_state_matrix

        if (np.abs(error) < precision).all():
            break

        state_matrix = new_state_matrix

        counter += 1
    
    return state_matrix


def get_aggregated_ranks(matrix):

    """Return the final aggregated ranks based on the stationary distribution matrix

    Args:
        matrix (numpy.ndarray): stationary distribution matrix

    Returns:
        list: final aggregated ranks
    """

    a = {}
    rank = 1
    
    for num in sorted(matrix, reverse = True):
        if num not in a:
            a[num] = rank
            rank = rank+1

    final_ranks = [a[i] for i in matrix]

    return final_ranks


def mc4_aggregator(file_path, header_row=0, index_col=0, precision=0.0000001, iterations=200, erg_number=0.15):

    """Performs aggregation on different ranks using Markov Chain Type 4 Rank Aggeregation algorithm and returns the aggregated ranks 

    Args:
        file_path (string): path of the dataset file containing all different ranks
        header_row (int or None): row number of the dataset containing the header, default is 0
        index_col (int or None): column number of the dataset containing the index, default is 0
        precision (float): acceptable error margin for convergence, default is 1e-07
        iterations (int): number of iterations to reach stationary distribution, default is 200
        erg_number (float): small,positive number used to calculate ergodic transition matrix, default is 0.15

    Returns:
        list: contestantwise aggregated ranks
    """

    if is_valid_path(file_path):

        df = get_dataframe(file_path, header_row=header_row,index_col=index_col)

        rows, cols = get_matrix_shape(df)

        partial_transition_matrix = get_partial_transition_matrix(df, rows, cols)

        normalized_transition_matrix = get_normalized_transition_matrix(partial_transition_matrix, rows)

        ergodic_transition_matrix = get_ergodic_transition_matrix(normalized_transition_matrix, rows, erg_number)

        initial_distribution_matrix = get_initial_distribution_matrix(rows)

        stationary_distribution_matrix = get_stationary_distribution_matrix(initial_distribution_matrix, ergodic_transition_matrix, precision, iterations)

        final_ranks = get_aggregated_ranks(stationary_distribution_matrix)
        
        return final_ranks
