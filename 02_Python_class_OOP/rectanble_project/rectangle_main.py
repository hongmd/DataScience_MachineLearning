from loguru import logger
from pathlib import Path
from argparse import ArgumentParser, HelpFormatter
import json, re


#-----------------------------------------------------------------------------------------------------------#
#--------------------------------- Define Class and its methods --------------------------------------------#
#-----------------------------------------------------------------------------------------------------------#

class RectangleCalculator:
    '''
    This class will takes the length and width of a rectangle as inputs, 
    then return the corresponding perimeter and area as outputs.

    It can also read inputs from multiple JSON files.
    The results can be returned in a specified JSON file.
    The class supports multicore computing.
    '''


    def __init__(self, input = None, output = None, length = None, width = None, cores = 2):
        '''
        input: the path leading to an input directory containing JSON files, or directly to a specified JSON file
        output: the path leading to on output directory to store the results in JSON files, or directly to a specified JSON file
        length: the length of the rectangle (for inplace calculating)
        width: the width of the rectangle (for inplace calculating)
        cores: the number of CPU cores using for parallel computing
        '''
        self.input = Path(input)
        self.output = Path(output)
        self.length = length
        self.width = width
        self.cores = cores


    def _load_rectangle_json(self, json_input_file):
        json_input_path = self.input.joinpath(json_input_file)
        with open(json_input_path, "r") as json_file_object:
            self.length, self.width = json.load(json_file_object).values()
    

    @staticmethod
    def validate_input(number):
        try:
            number = float(number)
        except Exception as e:
            logger.error(e)
            return None
        else:
            return number
    

    def _calculate(self):
        self.perimeter = 2 * (self.length + self.width)