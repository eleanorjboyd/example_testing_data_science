import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df["Nationality"] = df["Nationality"].str.title()
    return df


def get_active_drivers(file_path):
    df = load_data(file_path)
    active_df = df[df["Active"]]
    num = len(active_df)
    return num


def winning_per_nationality(file_path):
    df = load_data(file_path)
    wins_by_nation = df.groupby("Nationality")["Race_Wins"].sum()
    podiums_by_nation = df.groupby("Nationality")["Podiums"].sum()
    count_by_nationality = df["Nationality"].value_counts()

    win_ratio = wins_by_nation / count_by_nationality
    podium_ratio = podiums_by_nation / count_by_nationality
    return win_ratio, podium_ratio
