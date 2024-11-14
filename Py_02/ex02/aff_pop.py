from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt


def str_to_int(df) -> pd.DataFrame:
    """
    Converts string in scientific notation, then converts them to int.
    """
    df = df.str.replace('M', 'e6').str.replace('k', 'e3')
    df = df.astype(float)
    df = df.astype(int)
    return df


def aff_pop(df, country_1, country_2) -> None:
    """
    Displays a graph comparing population projections for two countries
    over a period
    """
    try:
        if country_1 == country_2:
            raise AssertionError("Need two different countries.")
        df_c1 = str_to_int(df[country_1][:-50])
        df_c2 = str_to_int(df[country_2][:-50])
        plt.plot(df_c2.index, df_c2, label=country_2)
        plt.plot(df_c1.index, df_c1, label=country_1, color='green')
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(df_c1.index[::40])
        plt.ylabel("Population")
        max_pop = max(df_c1.max(), df_c2.max())
        y_ticks = range(20000000, max_pop + 10000000, 20000000)
        plt.yticks(y_ticks, [f"{int(y/1e6)}M" for y in y_ticks])
        plt.legend(loc='lower right')
        plt.show()
    except KeyError:
        print(f"{KeyError.__name__}: The country does not exist in dataset.")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


def main():
    df = load("population_total.csv")
    aff_pop(df, "France", "Belgium")


if __name__ == "__main__":
    main()
