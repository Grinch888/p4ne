#!/usr/local/bin/python3
from openpyxl import load_workbook #Библиотека для работы с XLSX
from matplotlib import pyplot #Библиотека построения графов

#Загружаем файл XLSX в память
wb = load_workbook('./data_analysis_lab.xlsx')
sheet = wb['Data']

#Читаем данные из ячеек

def getvalue(x): return x.value #Функция получения значений из ячеек
#Создаем списки значений из столбцов
list_x = list(map(getvalue, sheet['A'][1:]))
list_y = list(map(getvalue, sheet['D'][1:]))
list_z = list(map(getvalue, sheet['C'][1:]))

#Рисуем граф
pyplot.plot(list_x, list_y, label="relationship")
pyplot.plot(list_x, list_z, label="activity")
pyplot.show()