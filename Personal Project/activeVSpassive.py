import pandas
from pathlib import Path

pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)


def readStocksData(code):
    filePath = Path(code + ".csv")
    if filePath.is_file():
        dataset = pandas.read_csv(filePath)
    else:
        print("Code '", code, "' do not exist")
        return None

    return dataset


def printStockHistory(code):
    data = readStocksData(code)
    print(data)


if __name__ == '__main__':
    APPLE = pandas.read_csv("APPLE.csv")
    TESLA = pandas.read_csv("TESLA.csv")
    VOO = pandas.read_csv("VOO.csv")

    # # checking if the dates are all the same for 5 years
    # count = 0
    # for i in range(1257, -1, -1):
    #     if APPLE.iloc[i]['Date'] == TESLA.iloc[i]['Date'] == VOO.iloc[i]['Date']:
    #         count += 1
    # print(count)

    portfolio = {"APPLE": 0.34, "TESLA": 0.33, "VOO": 0.33}

    initial = 100000
    start_date = 1257
    # passive
    apple_start_count = (initial * portfolio["APPLE"]) // float(APPLE.iloc[start_date]['Close/Last'][1:])
    apple_revenue = apple_start_count * float(APPLE.iloc[0]['Close/Last'][1:])

    tesla_start_count = (initial * portfolio["TESLA"]) // float(TESLA.iloc[start_date]['Close/Last'][1:])
    tesla_revenue = tesla_start_count * float(TESLA.iloc[0]['Close/Last'][1:])

    voo_start_count = (initial * portfolio["VOO"]) // float(VOO.iloc[start_date]['Close/Last'])
    voo_revenue = voo_start_count * float(VOO.iloc[0]['Close/Last'])

    print(f"passive net gain = {apple_revenue + tesla_revenue + voo_revenue}")

    tesla_price = float(TESLA.iloc[start_date]['Close/Last'][1:])
    apple_price = float(APPLE.iloc[start_date]['Close/Last'][1:])
    voo_price = float(VOO.iloc[start_date]['Close/Last'])

    tesla_count = int(initial * portfolio["TESLA"] // tesla_price)
    apple_count = int(initial * portfolio["APPLE"] // apple_price)
    voo_count = int(initial * portfolio["VOO"] // voo_price)

    cash_wallet = initial - tesla_count * float(TESLA.iloc[start_date]['Close/Last'][1:]) - apple_count * float(
        APPLE.iloc[start_date]['Close/Last'][1:]) - voo_count * float(VOO.iloc[start_date]['Close/Last'])

    stock_price = {"APPLE": apple_price,
                   "TESLA": tesla_price,
                   "VOO": voo_price}

    stock_count = {"APPLE": apple_count,
                   "TESLA": tesla_count,
                   "VOO": voo_count}

    stock_wallet = {"APPLE": apple_count * apple_price,
                    "TESLA": tesla_count * tesla_price,
                    "VOO": voo_count * voo_price}

    stock_wallet_sum = sum(stock_wallet.values())

    curr_portfolio = {"APPLE": stock_wallet["APPLE"] / stock_wallet_sum,
                      "TESLA": stock_wallet["TESLA"] / stock_wallet_sum,
                      "VOO": stock_wallet["VOO"] / stock_wallet_sum}

    trading_fee = 0.65
    trade_threshold = 0.05

    for day in range(1256, -1, -1):
        stock_price["TESLA"] = float(TESLA.iloc[day]['Close/Last'][1:])
        stock_price["APPLE"] = float(APPLE.iloc[day]['Close/Last'][1:])
        stock_price["VOO"] = float(VOO.iloc[day]['Close/Last'])

        stock_wallet = {"APPLE": stock_count["APPLE"] * stock_price["APPLE"],
                        "TESLA": stock_count["TESLA"] * stock_price["TESLA"],
                        "VOO": stock_count["VOO"] * stock_price["VOO"]}

        stock_wallet_sum = sum(stock_wallet.values())

        curr_portfolio = {"APPLE": stock_wallet["APPLE"] / stock_wallet_sum,
                          "TESLA": stock_wallet["TESLA"] / stock_wallet_sum,
                          "VOO": stock_wallet["VOO"] / stock_wallet_sum}

        # selling stage
        for stock in curr_portfolio.keys():
            if curr_portfolio[stock] - portfolio[stock] > trade_threshold:
                selling_count = int(stock_count[stock] * (curr_portfolio[stock] - portfolio[stock]) / portfolio[stock])
                stock_count[stock] -= selling_count
                cash_wallet += selling_count * stock_price[stock]
                cash_wallet -= trading_fee

        # buying stage
        cash_to_buy = (cash_wallet / 3) - trading_fee
        for stock in curr_portfolio.keys():
            buy_count = 0
            if cash_to_buy // stock_price[stock] > 0:
                buy_count = cash_to_buy // stock_price[stock]
            stock_count[stock] += buy_count
            cash_wallet -= buy_count * stock_price[stock]

        # print(curr_portfolio)
        # print(cash_wallet)
        # print(stock_wallet)
    print(f" active net gain = {sum(stock_wallet.values())}")
