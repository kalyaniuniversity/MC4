import argparse
from mc4.algorithm import mc4_aggregator

parser = argparse.ArgumentParser(description='Takes necessary inputs for mc4_aggegator')

parser.add_argument('source', type=str, help='source of the lists of ranks')
parser.add_argument('-a', '--algo', type=str, default='mc4', help='rank aggregation algorithm, mc4 or mct, default is mc4', choices=['mc4', 'mct'])
parser.add_argument('-o', '--order', type=str, default='row', help='order of the dataset, default is row', choices=['row', 'column'])
parser.add_argument('-hr', '--header_row', type=int, help='row number of the header, default is None')
parser.add_argument('-ic', '--index_col', type=int, help='column number of the index, default is None')
parser.add_argument('-p', '--precision', type=float, default=0.0000001, help='error of convergence, default is 1e-07')
parser.add_argument('-i', '--iterations', type=int, default=200, help='no of iterations, default is 200')
parser.add_argument('-e', '--erg_number', type=float, default=0.15, help='ergodic number, default is 0.15')

args = parser.parse_args()

def main():
    print(mc4_aggregator(args.source, args.algo ,args.order, args.header_row, args.index_col, args.precision, args.iterations, args.erg_number))