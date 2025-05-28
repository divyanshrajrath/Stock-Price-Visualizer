import yfinance as yf
import matplotlib.pyplot as plt
import os

def fetch_and_plot_stock(symbol):
    #Fetch data....
    data=yf.download(symbol, period='30d', interval='1d')

    if data.empty:
        print(f"No data found for {symbol}")

    #plotting the data....
    plt.figure(figsize=(10,5))
    plt.plot(data['Close'], label=f'{symbol} Closing Prices', color='blue')
    plt.title(f'{symbol} STOCK CLOSING PRICE (30 DAYS)')
    plt.xlabel('Date')
    plt.ylabel('Price(USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    #create output dir
    os.makedirs('plots', exist_ok=True)
    filename=f'plots/{symbol}_plot.png'
    plt.savefig(filename)
    print(f"Plot saved as {filename}")

if __name__=='__main__':
    symbol=input("Enter the stock symbol (eg. AAPL, TSLA): ").upper()
    fetch_and_plot_stock(symbol)
