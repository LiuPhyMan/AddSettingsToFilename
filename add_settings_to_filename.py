#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10:08 2018/8/4

@author:    Liu Jinbao
@mail:      liu.jinbao@outlook.com
@project:   RenameFile
@IDE:       PyCharm
"""
import os

def append_parameters(file_path):
    para_dict = dict()
    with open(file_path) as f:
        for _line in f:
            if 'Temperature' in _line:
                para_dict['Tmpr'] = _line.split(':')[-1].strip()
            if 'Exposure Time' in _line:
                para_dict['ExpsTime'] = _line.split(':')[-1].strip()
            if 'Number of Accumulations' in _line:
                para_dict['NumAcc'] = _line.split(':')[-1].strip()
            if 'Gain level' in _line:
                para_dict['Gain'] = _line.split(':')[-1].strip()
            if 'Grating Groove' in _line:
                _str = _line.split(':')[-1].strip()
                _str = '2400' if _str.startswith('2') else '1200'
                para_dict['Grating'] = _str
    new_path = file_path[:-4]
    for key in ('Tmpr', 'ExpsTime', 'NumAcc', 'Gain', 'Grating'):
        new_path = new_path + '_{key}[{value}]'.format(key=key, value=para_dict[key])
    new_path = new_path + '.asc'
    os.rename(file_path, new_path)

_path = r"D:\Exp_data\exp_2018.07.27"
for root, dirs, files in os.walk(_path):
    if files:
        for _file in files:
            if _file.endswith('.asc'):
                append_parameters(root + r'\\' + _file)
