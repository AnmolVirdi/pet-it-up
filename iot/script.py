import pandas as pd
import time


def getData():
    time.sleep(30)
    data = pd.read_json("https://sheetdb.io/api/v1/rliyonabq4f1v")
    lastCol = data.tail(1)
    lastCol = lastCol.to_numpy()

    return lastCol


print(getData())  # thrid and fourth value use krni bs
