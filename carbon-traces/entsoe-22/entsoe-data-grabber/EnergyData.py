"""
    EnergyData is used to get information about the energy mixture of the grid
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime, timedelta
from entsoe import EntsoePandasClient
from variables import CO2_worst, CO2_best, CO2_best_aggregated, EnergyTypeCat, graph_colors

import os


class EnergyData:

    def __init__(self, start: pd.Timestamp, end: pd.Timestamp,country_code: str, extension: str):

        self.start_date = start
        self.end_date = end
        self.country_code = country_code

        file_name = f"{extension}s/entso-e-{self.country_code}-{self.start_date.year}_{self.start_date.month}-{self.end_date.year}_{self.end_date.month}.{extension}"
        if os.path.exists(file_name):
            self.df = pd.read_parquet(file_name)
        else:
            self.client = EntsoePandasClient(api_key="b637f458-cdb7-4771-92bf-cfd49f3646d9")
            self.df = self.client.query_generation(self.country_code, start=self.start_date, end=self.end_date, psr_type=None)

            self.df.to_parquet(file_name)

        columns_to_delete = [c for c in self.df.columns if c[1] == 'Actual Consumption']
        self.df = self.df.drop(columns_to_delete, axis=1)

        # if the column names are tuples, we keep only the first element

        # if self.df.columns[1].toString() > 1:
        self.column_names = [c[0] for c in self.df.columns]
        # else: # else, if the column name is a string, we keep as it is
        self.column_names = [c[0] for c in self.df.columns]
        self.df = self.df.fillna(0)

        self.df["total_energy"] = self.df.sum(axis=1)
        self.df["carbon_usage"] = self.df.apply(self.get_carbon_usage, axis=1)
        self.df["carbon_intensity"] = self.df["carbon_usage"] / self.df["total_energy"]
        #
        # # Keep only 'carbon_intensity' and ensure timestamp is included
        self.df = self.df.reset_index()  # Reset the index to bring the timestamp as a column
        self.df = self.df[["index", "carbon_intensity"]]  # Keep only the required columns

        # Rename 'index' to 'timestamp' and carbon_intensity to 'carbon_intensity'
        self.df.rename(columns={"index": "timestamp", "carbon_intensity": "carbon_intensity"}, inplace=True)
        # self.df.rename(columns={"index": "timestamp"}, inplace=True)  # Rename 'index' to 'timestamp' and carbon_intensity to 'carbon_intensity'

        # Save to Parquet file
        if extension == "parquet":
            self.df.to_parquet(file_name, index=False)

    def add_carbon_stats(self):
        self.carbon_stats = {}

        for column_name in self.df.columns:
            self.carbon_stats[column_name] = {"worst": CO2_worst[column_name], "best": CO2_best[column_name]}

        worst_carbon = {x: self.carbon_stats[x]["worst"] for x in self.carbon_stats}

        self.column_names = list(dict(sorted(worst_carbon.items(), key=lambda item: item[1])).keys())

    def get_carbon_usage(self, serie):
        total_carbon = 0

        # write a file
        with open('carbon_usage.txt', 'a') as f:
            f.write(str(serie) + '\n')

        for column_name in self.column_names:
            if column_name == "total_energy":
                continue

            try:
                val = serie[column_name]
            except:
                val = 0

            # write the column name in file
            with open('carbon_usage.txt', 'a') as f:
                f.write(str(column_name) + '\n')

            total_carbon += val * CO2_best[column_name]

        return total_carbon

    # def get_energy_mix(self, timestamp):
    #     index = np.searchsorted(self.df.index, timestamp, side="right") - 1
    #
    #     return self.df.iloc[index]["carbon_intensity"]

    def __len__(self):
        return len(self.df.index)

