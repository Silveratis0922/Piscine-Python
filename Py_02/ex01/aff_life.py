from load_csv import load
import matplotlib.pyplot as plt


def aff_life(df) -> None:
    """
    Display the evolution of life expectancy for a given
    country on a graph using Matplotlib.
    """
    try:
        country = "Andorra"
        plt.plot(df.index, df[country])
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.xticks(df.index[::40])
        plt.ylabel("Life expectancy")
        plt.show()
    except KeyError:
        print(f"{AssertionError.__name__}: Country does not exist.")


def main():
    try:
        df = load("life_expectancy_years.csv")
        aff_life(df)
    except KeyboardInterrupt:
        print("Program ended with Ctrl + C.")


if __name__ == "__main__":
    main()
