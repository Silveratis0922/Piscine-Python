from load_csv import load
import matplotlib.pyplot as plt


def projection_life(df_life, df_income) -> None:
    try:
        if df_life.name != df_income.name:
            raise AssertionError("Comparaison must be on the same year.")
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
    df_life = load("life_expectancy_years.csv")
    df_inc = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    print(df_inc['1900'])
    projection_life(df_life['1900'], df_inc['1900'])


if __name__ == "__main__":
    main()
