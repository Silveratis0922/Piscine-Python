class calculator:
    """Class doctstring"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        # res = []
        # for i, j in zip(V1, V2):
        #     res.append(i * j)
        # print(f"Dot product is : {sum(res)}")
        print(sum(i * j for i, j in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        # res = []
        # for i, j in zip(V1, V2):
        #     res.append(float(i + j))
        # print(f"Add Vector is : {res}")
        print(f"Add Vector is : {list(float(i + j) for i, j in zip(V1, V2))}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        # res = []
        # for i, j in zip(V1, V2):
        #   res.append(float(i - j))
        # print(f"Sous Vector is: {res}")
        print(f"Sous Vector is: {list(float(i - j) for i, j in zip(V1, V2))}")
