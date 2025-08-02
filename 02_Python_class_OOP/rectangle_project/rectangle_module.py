from loguru import logger
from pathlib import Path
from argparse import ArgumentParser, HelpFormatter
import json, re, os
from termcolor import colored
import multiprocessing


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


    def __init__(self, input = '', output = '', length = None, width = None, cores = 2):
        '''
        input: the path leading to an input directory containing JSON files, or directly to a specified JSON file
        output: the path leading to on output directory to store the results in JSON files, or directly to a specified JSON file
        length: the length of the rectangle (for inplace calculating)
        width: the width of the rectangle (for inplace calculating)
        cores: the number of CPU cores using for parallel computing
        '''
        self.input = input
        self.output = output
        self.__length = length
        self.__width = width
        self.cores = cores

    
    @staticmethod
    def __valiate_input_number(*numbers): # Internal use only, cannot call out when the module is being imported
        numeric_pattern = r"^\d+\.?\d*$"
        numbers = list(numbers)
        for idx, number in enumerate(numbers):
            if re.match(numeric_pattern, str(number)):
                numbers[idx] = float(number)
            else:
                numbers[idx] = None
        
        return numbers


    def load_rectangle_json(self, json_rectangle_name):
        if len(Path(json_rectangle_name).parts) > 1:
            json_file_path = json_rectangle_name
        else:
            json_file_path = self.input.joinpath(json_rectangle_name)
        
        with open(json_file_path, "r") as json_pointer:
            length, width = json.load(json_pointer).values()
            length, width = RectangleCalculator.__valiate_input_number(length, width)
        
        if None in [length, width]:
            logger.warning(f"The inputs in this {json_rectangle_name} file are corrupted!!!")
        return length, width
    

    @property
    def perimeter(self):
        self.length, self.width = self.__valiate_input_number(self.length, self.width)
        if (self.length is None) or (self.width is None):
            self.__perimeter = None
        else:
            self.__perimeter = 2 * (self.length + self.width) # Name it as "self.__perimeter" to prevent user from changing its value 
       
        return self.__perimeter


    @property
    def area(self):
        self.length, self.width = self.__valiate_input_number(self.length, self.width)

        if (self.length is None) or (self.width is None):
            self.__area = None
        else:
            self.__area = self.length * self.width # Name it as "self.__area" to prevent user from changing its value
        return self.__area

    
    def save_file(self, json_rectangle_name):
        result_dict = {
            "length": self.length,
            "width": self.width,
            "perimeter": self.perimeter,
            "area": self.area
        }

        match len(json_rectangle_name.split(os.path.sep)):
            case 1:
                json_path = self.output.joinpath(json_rectangle_name)
            case _:
                json_path = self.output

        if not json_path.name.endswith(".json"):
            json_path =  Path(str(json_path)+".json")
            logger.warning(f"The output file name does not end with '.json', automatically set as {json_rectangle_name}.json")
        with open(json_path, "w") as json_pointer:
            json.dump(result_dict, json_pointer, indent = 4)
        
        if json_path.stem == "nameless":
            logger.info(f"Result is saved in {json_path}")
    

    def __validate_output_path(self):
        match str(self.output):
            case "":
                pass
            case _:
                if (len(str(self.output).split(os.path.sep)) == 1) or (not (Path(self.output).parent.is_dir())):
                    logger.error("The output path's parent directory does not exist!")
                    self.output = ""
                
                elif (Path(self.output).suffix != ""):
                    self.output = Path(self.output)
                    self.output = Path(self.output.parent, self.output.stem)
                    self.output.mkdir(exist_ok = True)
                    logger.warning(f"Your output path should be a directory, not a file, automatically set as {self.output}")
                
                else:
                    self.output = Path(self.output)
                    self.output.mkdir(exist_ok = True)
        
        return self.output

    
    def summary(self, json_rectangle_name = "nameless"):
        self.output = self.__validate_output_path()
        match str(self.output):
            case "":
                json_rectangle_name = colored(json_rectangle_name, "red", attrs = ["bold"])
                out_message = (
                    f"\n\nResult of {json_rectangle_name} rectangle:\n"
                    f"++ Length = {self.length}\n"
                    f"++ Width = {self.width}\n"
                    f"++ Perimeter = 2 * ({self.length} + {self.width}) = {self.perimeter}\n"
                    f"++ Area = {self.length} * {self.width} = {self.area}\n"
                )
                logger.info(out_message)
            case _:
                self.save_file(json_rectangle_name)


    def _SingleInput_WorkFlow(self, json_rectangle_name):
        if json_rectangle_name != '':
            self.length, self.width = self.load_rectangle_json(json_rectangle_name)
            
            if (None not in [self.__length, self.__width]):
                logger.warning(f"Detected valid inputs in {json_rectangle_name}, prioritize them for calculation.")
  
            self.summary(json_rectangle_name)
        
        elif None in [self.__length, self.__width]:
            logger.error("No valid inputs were given")
        
        else:
            self.length, self.width = self.__length, self.__width
            self.summary()
            

#------------------------------------------------------------------------------------------------------------#
#------------------------------------------ Define log_file() function --------------------------------------#
#------------------------------------------------------------------------------------------------------------#

def config_log_file(project_dir):
    # Add file sink while keeping the default console output
    logger_path = Path(project_dir).joinpath("rectangle_logs.txt")
    if logger_path.exists():
        logger_path.unlink()

    logger.add(sink = logger_path, # The path to the .txt file that saves logs
            rotation="1 MB",  # Rotate when file reaches 1MB
            retention="10 days",  # Keep logs for 10 days
            level="WARNING") # Only save the WARNING level and above


#------------------------------------------------------------------------------------------------------------#
#------------------------------------------ Define main() function ------------------------------------------#
#------------------------------------------------------------------------------------------------------------#

def main():
    try:
        calculator = RectangleCalculator(
            input = "02_Python_class_OOP/rectangle_project/data/",
            output = "02_Python_class_OOP/rectangle_project/result.txt/",
            length = 2,
            width = 3,
            cores = 4
        )

        if (calculator.input != "") and Path(calculator.input).exists():
            calculator.input = Path(calculator.input)
            config_log_file(calculator.input.parent)

            if calculator.input.suffix == ".json":
                calculator._SingleInput_WorkFlow(calculator.input)
            
            elif (calculator.input.is_dir()):
                input_files = [(entry.name,) for entry in calculator.input.glob("*.json")]
                calculator.output = calculator._RectangleCalculator__validate_output_path()

                match str(calculator.output):
                    case "":
                        logger.warning(
                            (   
                                "\nNo valid ouput directory path was given!!!"
                                "\nAll results will be printed here and will NOT be saved!!!"
                            )
                        )
                        
                        answer = input(colored("Would you like to proceed? [y/n]: ", "blue", attrs = ["bold"]))
                        if answer.lower() == "y":
                            with multiprocessing.Pool(processes = calculator.cores) as pool:
                                pool.starmap(func = calculator._SingleInput_WorkFlow, iterable = input_files)
                        else:
                            return None # stop the program
                        
                    case _:           
                        with multiprocessing.Pool(processes = calculator.cores) as pool:
                            pool.starmap(func = calculator._SingleInput_WorkFlow, iterable = input_files)
                        
                        logger.info(f"All result files are saved in {calculator.output}")

            else:
                logger.error("There are multiple input files, but the output directory path was not correctly specified")                          

        else:
            calculator._SingleInput_WorkFlow('')
    
    except Exception as e:
        logger.error(e)


#---------------------------------------------------------------------------------------------------------#
#------------------------------------------ Run main() function ------------------------------------------#
#---------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()
    logger.info("Program ended! Thank you!")