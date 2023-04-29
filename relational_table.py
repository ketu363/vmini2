from __future__ import annotations
from pathlib import Path
from typing import Union, Any, DefaultDict, Dict, Tuple
from .utils import read_csv


class RelationalTable:
    def __init__(self, src: Union[str, Path, DefaultDict]) -> None:
        if isinstance(src, str) or isinstance(src, Path):
            self.src = read_csv(src)
        else:
            self.src = src

        self.relations = {} 

    def _set(self) -> None:


        # Initialize an empty dictionary to hold the data
        self.data = {}

        # Loop over the row labels and initialize an empty dictionary for each row
        for key, items in self.src.items():
            # Loop over the column labels and set a value for each column in the row
            dataCol = {}
            for index, item in enumerate(items):
                dataCol[self.src.get('columns')[index]] = item

            self.data[key] = list(dataCol.items())
        
        """
        This function Tabularizes the data which can be indexed using rows and columns just like a Dataframe in pandas.

        -> Complete this function to create a realtional database out of this data. 
        -> You need to have a PRIMARY KEY in the database and a `checker` to ensure that the key is always unique.
        -> The data can be queried using (row, col) indices or (key, row) indices.
        """
        ...

    def query(self, key: Union[Tuple[Any, Any], int, str], method="key-row") -> Any:
        """Complete this function so that the data can be queried using keys"""
        if method not in ["key-row", "row-col", "row", "col"]:
            raise ValueError("Invalid Argument `method`")
        
        if method == 'key-row':
            if type(key) is tuple:
                row = key[0]
                col = key[1]
            else:
                raise ValueError("incorrect value provided")
            print("value at ", key, " is: ", dict(self.data[str(col)])[row])

            
            ...
        elif method == 'row-col':
            
            if type(key) is tuple:
                row = key[0]
                col = key[1]
            else:
                raise ValueError("incorrect value provided")

            print("value at ", key, " is: ", self.data[str(row)][col][1])
            ...
        elif method == 'row':
            if type(key) is int:
                row = key
            else:
                raise ValueError("incorrect value provided")
            print("value at ", key, " is: ", self.data[str(row)])
            ...
        elif method == 'col':
            """Do Note that col can have an `int` or a `string` value"""
            
            if type(key) is int:
                row = key
                print("value at col ", key, " is: ", [j[key][1] for i, j in self.data.items()])
            elif type(key) is str:
                row = key
                print("value at col ", key, " is: ", [dict(j)[key] for i, j in self.data.items()])
            else:
                raise ValueError("incorrect value provided")
            ...

    def relate(self, other_table: RelationalTable, key):
        """Complete this function so that it can relate this table to another using a provided key"""
        def relate(self, other_table: RelationalTable, key):
            """Complete this function so that it can relate this table to another using a provided key"""
       


            if not isinstance(other_table, RelationalTable):
                raise ValueError("Invalid Argument: `other_table` must be of type `RelationalTable`")

            if key not in self.src.get('columns'):
                raise ValueError(f"Key {key} not found in table")

            if key not in other_table.src.get('columns'):
                raise ValueError(f"Key {key} not found in other_table")

            # Initialize an empty dictionary to hold the relation data
            relation_data = {}

            # Loop over the rows in this table
            for row_key, row_data in self.data.items():
                # Get the value of the key column for this row
                key_value = dict(row_data)[key]

                # Loop over the rows in the other table to find matching key value
                for other_row_key, other_row_data in other_table.data.items():
                    other_key_value = dict(other_row_data)[key]
                    if other_key_value == key_value:
                        # If the key values match, add a relation between the two rows
                        if row_key not in relation_data:
                            relation_data[row_key] = []
                        relation_data[row_key].append(other_row_key)

            # Store the relation data in the `relations` dictionary
            self.relations[other_table] = relation_data

        