import pandas as pd
import matplotlib.pyplot as plt

def load(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print("Loading dataset of dimensions", df.shape)
    plt.plot(df[1:])
    plt.title("Titre ici")
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.show