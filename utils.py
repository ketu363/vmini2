from pathlib import Path
from typing import Union
from collections import defaultdict
from pprint import pprint

def _selective_float(data):
    try:
        return float(data)
    except:
        return data


def read_csv(path: Union[str, Path], 
             delimitor: str=',', 
             index: bool=True, 
             verbose: bool=False) -> defaultdict:
    """This is a simple function to read_csv files. It is recommneded that you use data with ',' as delimitors as this
    has not been stress tested for other delimitors though it is a high chance that this would work.

    Parameters
    ----------
    path : Union[str, Path]
        Path to the csv file. If you get a FileNotFoundError You have not specified the correct path.
    delimitor : str, optional
        The delimitor used to seperate the data in CSV file, by default ','
    index : bool, optional
        Index the data by default providing it a unique key, by default True
    verbose : bool, optional
        Print out the read data, by default False

    Returns
    -------
    defaultdict
        Returns a dictionary of data with row number as key and data stored in a list. 
        Run with the verbose argument to see how it looks
    """
    with open(path, "r") as file:
        data: list[str] =  file.readlines()

    print("\n\n", data, "\n\n")
    csv_file: defaultdict = defaultdict(list)
    csv_file["columns"] = data[0].strip().split(f"{delimitor}") 
    
    if index:
        csv_file["columns"].insert(0, "Index")

    for idx, line in enumerate(data[1:]):
        listed = [idx] + list(map(_selective_float, line.strip().split(f"{delimitor}")))
        csv_file[str(idx)] = listed

    if verbose:
        print("\n\nThe Following Data was read ...\n\n")
        pprint(csv_file, indent=4)

    return csv_file


if __name__ == '__main__':
    data = read_csv("data/IRIS.csv", verbose=True)
    # pprint(data, indent=4)