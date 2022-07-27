import twstock
class Basic():
    #昨日收盤價
    def close(stock):
        stock = twstock.Stock(stock)
        return stock.price

    def limit_up(open):
        limit = float(open)*1.1
        return round(limit,2)
    
    def limit_down(open):
        limit = float(open)*0.9
        return round(limit,2)