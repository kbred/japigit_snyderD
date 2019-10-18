import requests
import pprint

def getStockData(stock_symbol):
    api_key = "C9Q5T9EM0RJT60CH"
    request_url = "https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=" + stock_symbol +"&apikey=" + api_key
    response = requests.get(request_url)
    json_reponse = response.json()
    return json_reponse


def main():
    output_list = []
    while True:
        print()
        stock_symbol = input("Enter Stock Symbol(or press ENTER to quit): " ) 
        
        if stock_symbol == '':
            break
        
        stock_data_json = getStockData(stock_symbol)
        
        print("Json Response: ", stock_data_json) 
                
        stock_data_dictionary = stock_data_json['Stock Quotes'][0]
        
        price = stock_data_dictionary['2. price']

        string_to_print = "The current price of " + stock_symbol + " is: " + str(price)
        
        print(string_to_print)
        output_list.append(string_to_print)

    file_name = "japi.out"

    with open(file_name, "w+") as file:
        len_list = len(output_list)
        for i in range(0, len_list):
            file.write(str(output_list[i]))
            if i < len_list - 1:
                file.write("\n")

main()
print() 
print("Good Bye")