import pandas as pd
import matplotlib.pyplot as plt


def load(path: str) -> pd.DataFrame:
    country = "Italy"
    df = pd.read_csv(path, index_col="country").T
    print("Loading dataset of dimensions", df.shape)
    plt.plot(df.index, df[country])
    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.xticks(1800, 2101, 40)
    plt.ylabel("Life expectancy")
    plt.show()
