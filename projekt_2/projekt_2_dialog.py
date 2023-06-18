# -*- coding: utf-8 -*-
"""
/***************************************************************************
 WtyczkaProjektDialog
                                 A QGIS plugin
 obliczanie pola i różnicy wysokości
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2023 by E.S.,D.G.
        email                : 01169919@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface
from qgis.core import *


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'projekt_2_dialog_base.ui'))


class WtyczkaProjektDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(WtyczkaProjektDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.pushButton_wysokosc.clicked.connect(self.policz_punkty)
        self.pushButton_wysokosc.clicked.connect(self.wysokosc)
        self.pushButton_pole.clicked.connect(self.pole)

    def policz_punkty(self):
        number_of_selected_features = len(self.mMapLayerComboBox_warstwa.currentLayer().selectedFeatures())
        
    def wysokosc(self):
        warstwa = self.mMapLayerComboBox_warstwa.currentLayer()
        wspolrzedne = warstwa.selectedFeatures()
        H = []
        lista_nazwa = []
        for kolumna in wspolrzedne:
            h = kolumna["H"]
            H.append(h)
            nazwa = kolumna["EntityHandle"]
            lista_nazwa.append(nazwa)
        if len(H) > 2:
            wybrane = len(H)
            self.label_wysokosc.setText(f'Wymagana ilość: 2. Wybrano {wybrane}.')
        elif len(H) < 2:
            wybrane = len(H)
            self.label_wysokosc.setText(f'Wymagana ilość: 2. Wybrano {wybrane}.')
        else:
            wynik = H[1] - H[0]
            pkt1 = lista_nazwa[0]
            pkt2 = lista_nazwa[1]
            self.label_wysokosc.setText(
                f'Różnica wysokości między punktami {pkt1} a {pkt2} to {wynik} [m]')
      
    def pole(self):
        warstwa = self.mMapLayerComboBox_warstwa.currentLayer()
        wspolrzedne = warstwa.selectedFeatures()
        nr = []
        for kolumna in wspolrzedne:
            n = float(kolumna["X"])
            nr.append(n)
        ile = len(nr)
        punkty = []
        for punkt in wspolrzedne:
            punkty.append(punkt.geometry().asPoint())
        if ile == 0:
            self.label_pole.setText('Nie wybrano żadnych punktów.') 
        if punkty[0] != punkty[-1]:
            punkty.append(punkty[0])
        
        pole = 0
        if ile >= 3:
            for i in range(ile - 1):
                x1, y1 = punkty[i]
                x2, y2 = punkty[i + 1]
                pole += (x1 * y2 - x2 * y1)
            pole_dokl = round(abs(pole)/2,5)
            self.label_pole.setText(f'Pole pomiędzy wybranymi {ile} punktami = {pole_dokl} m^2')
         
        else:
            self.label_pole.setText('Za mało. Należy wybrać 3 lub więcej punktów.')