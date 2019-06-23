import pandas as pd
import os.path


class Excel:

    def __init__(self):
        self.__header = ['Algorithm', 'dimension', 'Bench', 'Min', 'Max', 'Mean', 'Median', 'Std']

    def tableToDataFrame(self, table):
        df = pd.DataFrame.from_records(table, columns=self.__header)
        return df

    def exporttocsv(self, dataframe, name):
        dataframe.to_csv(r'D:\Žan\Feri ITK\3Letnik\Diploma\program\\' + str(name) + '.csv', index=None, header=True)

    @property
    def header(self):
        return self.__header

    def export_to_sheets(self, df, name):
        path = r'D:\Žan\Feri ITK\3Letnik\Diploma\program\\' + name + '.xlsx'
        try:
            if os.path.isfile(path):
                xls_file = pd.ExcelFile(path)
                dfexisting = xls_file.parse('Sheet1')
                combined_data = dfexisting.append(df, ignore_index=True)
                writer = pd.ExcelWriter(path, engine='xlsxwriter')
                combined_data.to_excel(writer, index=False)
                writer.save()
            else:
                writer = pd.ExcelWriter(path, engine='xlsxwriter')
                df.to_excel(writer, index=False)
                writer.save()
        except FileNotFoundError:
            print("file ne obstaja")

