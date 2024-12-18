from load_csv import load
import matplotlib.pyplot as plt


def projection_life(df_life, df_income) -> None:
    """
    Plots a scatter graph of life expectancy versus GDP for a given year.
    """
    try:
        if df_life.name != df_income.name:
            raise AssertionError("Comparaison must be on the same year.")
        if df_life.name != '1900':
            raise AssertionError("You must display the year 1900.")
        plt.scatter(df_income.values, df_life.values)
        plt.title(df_life.name)
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.show()
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


def main():
    try:
        life = load("life_expectancy_years.csv")
        inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        projection_life(life['1900'], inc['1900'])
    except KeyboardInterrupt:
        print(f"{AssertionError.__name__}: Program end with Ctrl + C.")


if __name__ == "__main__":
    main()
