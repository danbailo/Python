#pip3 install --upgrade chardet --user

import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Making a list of currencies
currencyList = ['AED', 'AUD', 'BHD', 'BRL', 'CAD', 'CNY', 'EUR', 'HKD', 'INR', 'USD']

def CreateWidgets():
    inputAMTL = Label(root, text="Digite o valor:", bg="SpringGreen4")
    inputAMTL.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

    inputAMTTxt = Entry(root, width=20, textvariable=getAMT)
    inputAMTTxt.grid(row=1, column=3, columnspan=2, pady=10)

    fromLabel = Label(root, text="De:", bg="SpringGreen4")
    fromLabel.grid(row=2, column=1)

    root.fromCombo = ttk.Combobox(root, values=currencyList)
    root.fromCombo.grid(row=2, column=2)

    toLabel = Label(root, text="Para:", bg="SpringGreen4")
    toLabel.grid(row=2, column=3)

    root.toCombo = ttk.Combobox(root, values=currencyList)
    root.toCombo.grid(row=2, column=4)
    
    convertButton = Button(root, text="Converter", width=52, command=Convert)
    convertButton.grid(row=3, column=1, columnspan=4, padx= 10, pady=10)

    outputAMTL = Label(root, text="VALOR CONVERTIDO:", font=('Helvetica', 10), bg="SpringGreen4")
    outputAMTL.grid(row=4, column=2, columnspan=2, pady=50)

    
    root.outputAMTAns = Label(root, font=('Helvetica', 20), bg="SpringGreen4")
    root.outputAMTAns.grid(row=4, column=3, columnspan=2, pady=50)

# Defining Convert() for converting the currency
def Convert():
    # Fetching and storing the user-inputs in resepective variables
    inputAmt = float(getAMT.get())
    fromCur = root.fromCombo.get()
    toCur = root.toCombo.get()

    # Storing the API Key from https://www.alphavantage.co/
    apiKey = "GET_ANY_KEY_FROM_ALPHAVANTAGE"

    #storing the base URL
    baseURL = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

    #storing the complete URL
    inputURL = baseURL + "&from_currency=" + fromCur + "&to_currency=" + toCur + "&apikey=" + apiKey

    #returning the responde object using get() of request
    requestObj = requests.get(inputURL)

    #converting the json format data to python dictionary
    result = requestObj.json()

    #debugger
    #print(result)
    #print('alo')

    #getting the exchange rate (required information)
    exchanceRate = float(result['Realtime Currency Exchange Rate']
                                              ['5. Exchange Rate'])

    #calculating the converted amount and rouding the decimal to 2 places
    calculateAmt = round(inputAmt * exchanceRate, 2)

    #Displaying the converted amount in the respective label
    root.outputAMTAns.config(text=str(calculateAmt))

if __name__ == "__main__":
    # creating object of tk class
    root = tk.Tk()

    #setting the title, background color and size of
    #the tkinter window and disabling the resizing property
    root.geometry("465x250")
    root.resizable(False, False)
    root.title("PyCurrencyConverter")
    root.config(bg = "SpringGreen4")

    #creating tkinter variables
    getAMT = StringVar()

    #calling the CreateWidgets() function
    CreateWidgets()

    #defining infinite loop to run application
    root.mainloop()
