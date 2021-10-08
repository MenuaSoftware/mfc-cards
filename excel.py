import pandas as pd

class excel:
    def __init__(self):
        df = pd.read_excel("assets/test.xlsx")
        print(df)


if __name__ == '__main__':
    excel()