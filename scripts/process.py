#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
from urllib import request
import datetime
import csv
import xlrd


source = 'http://www.imf.org/external/np/res/commod/External_Data.xls'

def setup():
	'''Crates the directories for archive and data if they don't exist
	
	'''
	if not os.path.exists('archive'):
		os.mkdir('archive')

def retrieve(source):
	'''Downloades xls data to archive directory
	
	'''
	request.urlretrieve(source,'archive/external-data.xls')

def process():
	'''Gets the data from xls file and puts them in seperete csv files for each comoditie
	
	'''		
	
	header = [
		'Date',
		'All Commodity Price Index',
		'Non-Fuel Price Index',
		'Food and Beverage Price Index',
		'Food Price Index',
		'Beverage Price Index',
		'Industrial Inputs Price Index',
		'Agricultural Raw Materials Index',
		'Metals Price Index',
		'Fuel Energy Index',
		'Crude Oil petroleum',
		'Aluminum',
		'Bananas',
		'Barley',
		'Beef',
		'Coal',
		'Cocoa beans',
		'Coffee Other Mild Arabicas',
		'Coffee Robusta',
		'Rapeseed oil',
		'Copper',
		'Cotton',
		'Fishmeal',
		'Groundnuts peanuts',
		'Hides',
		'China import Iron Ore Fines 62% FE spot',
		'Lamb',
		'Lead',
		'Soft Logs',
		'Hard Logs',
		'Maize corn',
		'Natural Gas - Russian Natural Gas border price in Germany',
		'Natural Gas - Indonesian Liquefied Natural Gas in Japan',
		'Natural Gas - Spot price at the Henry Hub terminal in Louisiana',
		'Nickel',
		'Crude Oil - petroleum-simple average of three spot prices',
		'Crude Oil - petroleum - Dated Brent light blend',
		'Oil Dubai',
		'Crude Oil petroleum - West Texas Intermediate 40 API',
		'Olive Oil',
		'Oranges',
		'Palm oil',
		'Swine - pork',
		'Poultry chicken',
		'Rice',
		'Rubber',
		'Fish salmon',
		'Hard Sawnwood',
		'Soft Sawnwood',
		'Shrimp',
		'Soybean Meal',
		'Soybean Oil',
		'Soybeans',
		'Sugar European import price',
		'Sugar Free Market',
		'Sugar U.S. import price',
		'Sunflower oil',
		'Tea',
		'Tin',
		'Uranium',
		'Wheat',
		'Wool coarse',
		'Wool fine',
		'Zinc'
	]
	
	with xlrd.open_workbook('archive/external-data.xls') as xls_data:
		sheet = xls_data.sheet_by_index(0)
		col_num = sheet.ncols
		row_num = sheet.nrows
		with open('data/commodity-prices.csv', 'w') as csv_file:
			csvwriter = csv.writer(csv_file)
			csvwriter.writerow(header)
			for row in range(4, row_num):
				csv_row = []
				for col in range(col_num):		
					if not col:				
						date = datetime.date(int(sheet.cell_value(row, col).split('M')[0]), int(sheet.cell_value(row, col).split('M')[1]), 1)		
						csv_row.append(date)
					else:
						price = sheet.cell_value(row, col)
						csv_row.append(price)
				csvwriter.writerow(csv_row)
			
if __name__ == '__main__':
	setup()
	retrieve(source)
	process()
