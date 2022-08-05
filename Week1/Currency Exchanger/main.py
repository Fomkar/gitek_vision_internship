import sys
import requests
from PyQt5 import QtWidgets
from WindowDesign import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App, self).__init__()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self)
        self.InitUI()
    
    def InitUI(self):
        self.UI.convert_button.clicked.connect(self.Convert)
    
    def Convert(self):
        base_currency = self.UI.currency_input.text()
        money_amount = float(self.UI.amount_input.text())
        currencies = self.UI.centralwidget.findChildren(QtWidgets.QCheckBox)
        
        symbols = ""
        for currency in currencies:
            if currency.isChecked():
                symbols += currency.text() + ","
        currency_symbols = symbols[:-1]
        
        parameters = {'base': base_currency,
                      'amount': money_amount,
                      'symbols': currency_symbols}
        
        response = requests.get(url = 'https://api.exchangerate.host/latest', params = parameters)
        data = response.json()['rates']
        
        result = ""
        for item in data.items():
                result += f"{money_amount} {base_currency} = {item[1]:.2f} {item[0]}" + "\n"
        
        self.UI.result_label.setText(result)

        
        

def StartApp():
    application = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(application.exec_())

StartApp()