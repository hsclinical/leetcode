#!/usr/bin/python3

"""
template.py

    Author: XX XXX

    Last Update: 2020/12/06

    Current Version: 1.0.0

    Log:
    Ver 1.0.0, Date: Aug 05, 20xx 
        Add yyy
    Ver 0.0.1, Date: May 12, 20xx
        Update xxx

    Decription: this is a template of python code to detemine the coding style
"""

import argparse, os, sys, logging, subprocess, time
from pathlib import Path
from os import path as ospath
import xml.etree.ElementTree as ET
import psycopg2 as pg
import sequencerHtmlParser
from concurrent.futures import ProcessPoolExecutor as Pool
from concurrent.futures import as_completed
import collections
from os import listdir
import pandas as pd

# Section - Log
pdLogger = logging.getLogger('pdLogger')
##Multiple calls to getLogger() with the same name will always return a reference to the same Logger object.
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
pdLogger.setLevel(logging.INFO)

pdOutHandler = logging.FileHandler('stdout.log')
pdOutHandler.setLevel(logging.INFO)
pdOutHandler.setFormatter(formatter)

pdErrHandler = logging.FileHandler('stderr.err')
pdErrHandler.setLevel(logging.ERROR)
pdErrHandler.setFormatter(formatter)

pdLogger.addHandler(pdOutHandler)
pdLogger.addHandler(pdErrHandler)

pdLogger.info('Start, let\s go')
pdLogger.error('Bug free. Pass to the end')

# Section - Class
class ExampleName(object):
    variableDict = {}
    variableList = []

    def __init__(self, args):
        self.a_param = args.a_param
        self.b_param = args.b_param
        self.c_param = args.c_param
        self.d_param = args.d_param

    def funcA(self, param):
        pass

    def funcB(self, param):
        pass

    def main(self):
        self.funcA(self.variableDict)
        self.funcB(self.variableList)
        pdLogger.info('Done')
        pdLogger.error('Done')

# Section - To parse and check agrv
if __name__ == '__main__':  
    parser = argparse.ArgumentParser(description='Parameters for ??? script')
    parser.add_argument('-a', '--a_param',  help = 'aaaa', default = 'xxx', type = str, choices = ['xxx', 'yyy'])
    parser.add_argument('-b', '--b_param',  help = 'bbbb', default = 1, type = int, choices = [1, 2])
    parser.add_argument('-c', '--c_param',  help = 'cccc', default = 2, type = int)
    parser.add_argument('-dd', '--d_param', help = 'dddd', default = 1, type = int, choices = [0, 1])

    args = parser.parse_args()
    if args.c_param > 10 or args.c_param <= 0:
        print('Please enter a valid number, see -h for help')
    eName = ExampleName(args)
    eName.main()
