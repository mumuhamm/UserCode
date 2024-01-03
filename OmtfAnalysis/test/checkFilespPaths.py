from pathlib import Path
import copy
import os
import random
import sys
import re
from os import listdir
from os.path import isfile, join
import glob



def get_file_list(prefix_path):
    prefix_path = Path(prefix_path)
    file_list = list(prefix_path.glob('*.root'))
    file_list = ['file:' + str(file.absolute()) for file in file_list]
    return file_list
    
prefix_path_1 = '/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch0_iPt0_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_145635/0000/'
prefix_path_2 = '/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch0_iPt1_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_150000/0000/'
prefix_path_3 = '/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch0_iPt2_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_150301/0000/'
prefix_path_4 = '/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch2_iPt0_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_145832/0000/'
prefix_path_5 = '/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch2_iPt1_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_150134/0000/'
prefix_path_6 = '/eos/user/a/almuhamm/ZMu_Test/Displaced13_1_0_04_11_2023/DisplacedMu_ch2_iPt2_Run2023_13_1_0_04_11_2023/13_1_0_04_11_2023/231104_150445/0000/'


file_list_1 = get_file_list(prefix_path_1)
file_list_2 = get_file_list(prefix_path_2)
file_list_3 = get_file_list(prefix_path_3)
file_list_4 = get_file_list(prefix_path_4)
file_list_5 = get_file_list(prefix_path_5)
file_list_6 = get_file_list(prefix_path_6)

all_files = file_list_1 + file_list_2 + file_list_3 + file_list_4 + file_list_5 + file_list_6

# Print or use the combined file list as needed
print(all_files)
