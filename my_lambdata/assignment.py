

from pandas import DataFrame



def add_state_names(my_df):
    # todo: add a column of corresponding state names

    names_map = {"CA":"Cali","CO":"Colo","CT":"Conn"}

    ##breakpoint()

    return my_df


if __name__ == "__main__":
    

    df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2.head())
