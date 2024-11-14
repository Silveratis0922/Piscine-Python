from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def aff_life(df) -> pd.DataFrame:
    """
    Display the evolution of life expectancy for a given
    country on a graph using Matplotlib.
    """
    country = "France"
    plt.plot(df.index, df[country])
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(df.index[::40])
    plt.ylabel("Life expectancy")
    plt.show()
    return df


def main():
    df = load("life_expectancy_years.csv")
    print(aff_life(df))


if __name__ == "__main__":
    main()
