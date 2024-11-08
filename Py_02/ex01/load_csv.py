import pandas as pd
import matplotlib.pyplot as plt


# def load(path: str) -> pd.DataFrame:
#     country = "Andorra"
#     df = pd.read_csv(path, index_col="country").T
#     print("Loading dataset of dimensions", df.shape)
#     plt.plot(df.index, df[country])
#     plt.title(f"{country} Life expectancy Projections")
#     plt.xlabel("Year")
#     plt.xticks(df.index[::40])
#     plt.ylabel("Life expectancy")
#     plt.show()
#     return df


def load(path: str) -> pd.DataFrame:
    country = "France"
    df = pd.read_csv(path, index_col="year")
    df = df.loc[df['country'] == country]
    print(df)
    # print("Loading dataset of dimensions", df.shape)
    # plt.plot(df.index, df)
    # plt.title(f"{country} Life expenctancy Projections")
    # plt.xlabel("Year")
    # plt.xticks(ticks=range(1800, 2101, 40))
    # plt.ylabel("Life expectancy")
    # plt.show()