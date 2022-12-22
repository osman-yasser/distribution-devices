# __main__.py
"""
    this module contain main function.
"""
import os

import numpy as np
import pandas as pd

from cli import read_user_cli_args
from perm import permute

from decorators.timing_functions import timer

def get_info(user_args) -> dict:
    _info = dict()
    _info['devices'] = user_args.devices
    _info['test_cases'] = user_args.test_cases
    _info['meridians'] = user_args.meridians
    _info['latitudes'] = user_args.latitudes
    return _info

def get_perm_table(_info: dict) -> np.ndarray:
    point = _info['meridians'] * _info['latitudes']
    perm_obj = permute([i for i in range(1, point+1)], _info['devices'])
    return perm_obj.random_sampling(_info['test_cases'])

@timer
def main() -> None:
    """RUN random permutation"""
    user_args = read_user_cli_args()
    _info = get_info(user_args)
    devices = [chr(65+i) for i in range(_info['devices'])]
    np_arry = get_perm_table(_info)
    df = pd.DataFrame(data=np_arry, columns=devices)
    cwd = os.getcwd()
    df.to_csv(f'{cwd}/results/result.csv')
    df.to_excel(f'{cwd}/results/result.xlsx')
    print('SUCESS! :)')


if __name__ == '__main__':
    main()