import pandas

if __name__ == '__main__':
    VOO = pandas.read_csv("VOO.csv")

    wallet = 700
    income = 700

    start_date = 1256 - 0
    curr_month = VOO.iloc[start_date]['Date'][1]
    stock_count = income / VOO.iloc[start_date]['Close/Last']

    print(VOO.iloc[start_date]['Date'], stock_count)
    for day in range(start_date, -1, -1):
        if curr_month != VOO.iloc[day]['Date'][1]:
            curr_month = VOO.iloc[day]['Date'][1]
            stock_count += income / VOO.iloc[day]['Close/Last']
            wallet += 700
            print(VOO.iloc[day]['Date'], stock_count)

    print(f"last price: ${VOO.iloc[day]['Close/Last']}")
    print(f"stock count: {stock_count}")
    print(f"total worth: ${stock_count * VOO.iloc[day]['Close/Last']}")
    print(f"total worth: ${stock_count * VOO.iloc[day]['Close/Last'] / 10}")
    print(f"total growth: {stock_count * VOO.iloc[day]['Close/Last'] / wallet * 100:.2f}%")




