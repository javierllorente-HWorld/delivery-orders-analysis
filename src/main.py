import os
import pandas as pd

INPUT_FILE = "data/orders.csv"
OUTPUT_DIR = "output"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    orders_by_city = df["city"].value_counts().reset_index()
    orders_by_city.columns = ["city", "total_orders"]

    revenue_by_city = df.groupby("city")["amount"].sum().reset_index()
    revenue_by_city.columns = ["city", "total_revenue"]

    orders_by_status = df["status"].value_counts().reset_index()
    orders_by_status.columns = ["status", "total_orders"]

    orders_by_city.to_csv(f"{OUTPUT_DIR}/orders_by_city.csv", index=False)
    revenue_by_city.to_csv(f"{OUTPUT_DIR}/revenue_by_city.csv", index=False)
    orders_by_status.to_csv(f"{OUTPUT_DIR}/orders_by_status.csv", index=False)

    print("Reportes generados correctamente")
    print("--------------------------------")
    print("output/orders_by_city.csv")
    print("output/revenue_by_city.csv")
    print("output/orders_by_status.csv")


if __name__ == "__main__":
    main()