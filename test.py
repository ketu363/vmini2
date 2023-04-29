from typing import Union
from pathlib import Path
from .relational_table import RelationalTable

PATH: Path = Path("")

def is_interactive():
    import __main__ as main
    return not hasattr(main, '__file__')

if is_interactive():
    PATH = Path("data/IRIS.csv")
else:
    PATH = Path(__file__).resolve() / "data" / "IRIS.csv"


if __name__ == '__main__':
    # Put any other arguments that you have added in the below list
    args = []

    table1 = RelationalTable(PATH, *args)
    table1._set()

    query_key : Union[int, str, tuple] = "..." ## Add the query key here

    values = table1.query(query_key)

    CUSTOM_DATA_PATH = Path("path/to/custom/data")
    table2 = RelationalTable(CUSTOM_DATA_PATH)

    table1.relate(table2, "foriegn_key")