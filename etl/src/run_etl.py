from extract import extract
from transform import transform
from load import load


def run_etl():
    extracted_dfs = extract()
    transformed_dfs = transform(extracted_dfs)
    load(transformed_dfs)


if __name__ == "__main__":
    run_etl()
