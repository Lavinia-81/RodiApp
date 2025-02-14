import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from roady_gui import Ui_MainWindow

from utils.init_config import config
from utils.distance import Distance
from roady import Roady
from utils.gas import Gas
import logging



LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s- %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
                    datefmt="%d-%m-%y %H:%M:%S",
                    handlers=[
                        logging.FileHandler("app.log"),
                        logging.StreamHandler()
                    ])


def is_input_checked():
    if ui.departure_city_lineEdit.text() and ui.destination_city_lineEdit_2.text():
        departure_city = ui.departure_city_lineEdit.text().capitalize()
        destination_city = ui.destination_city_lineEdit_2.text().capitalize()
        ui.departure_city_lineEdit.setText(departure_city)
        ui.destination_city_lineEdit_2.setText(destination_city)
        if ui.persons_lineEdit_3.text() and ui.consumption_lineEdit_4.text():
            if ui.persons_lineEdit_3.text().isnumeric() and ui.consumption_lineEdit_4.text().isnumeric():
             return True
            else:
                QMessageBox.warning(title="Error", text="Please input numbers for person and consumption.")
                LOGGER.error("Please input numbers for person and consumption.")
                return False
        else:
            QMessageBox.warning(text="Please add numbers of person and consumption.")
            LOGGER.error("Please add numbers of person and consumption.")
            return False
    else:
        QMessageBox.warning(text="Please enter a valid city.")
        LOGGER.error("Please enter a valid city.")

        return False



def calculate_price():
    if is_input_checked():

        dist = Distance(departure_city=ui.departure_city_lineEdit.text(),
                        destination_city=ui.destination_city_lineEdit_2.text(),
                        config=config)

        if ui.gas_comboBox.currentText() == "Gas":
            gas_price = Gas(config)
        else:
            # TODO create disel class which inherits fuel
            pass

        roady = Roady(dict, gas_price)

        price = roady.calculate_price(int(ui.persons_lineEdit_3()),
                                      float(ui.consumption_lineEdit_4.text()),
                                      ui.one_way_radioButton_2.isChecked(),
                                      ui.return_radioButton.isChecked())
                                      # ui.currency_comboBox.currentText())

        QMessageBox.information(title="Calculate price", text=f"Every person must pay: {int(price)}")
        LOGGER.info(f"Every person must pay: {int(price)}")
    # print(ui.departure_city_lineEdit.text())


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.calculate_pushButton.clicked.connect(calculate_price)
    MainWindow.show()
    sys.exit(app.exec())
