#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import urllib
import datetime
import csv
import xlrd

source = 'http://www.imf.org/external/np/res/commod/External_Data.xls'


def setup():
	'''Crates the directories for archive and data if they don't exist
	
	'''
	if not os.path.exists('../archive'):
		os.mkdir('../archive')
	if not os.path.exists('../data'):
		os.makedirs('../data')

def retrieve(source):
	'''Downloades xls data to archive directory
	
	'''
	urllib.urlretrieve(source,'../archive/external-data.xls')

def process():
	'''Gets the data from xls file and puts them in seperete csv files for each comoditie
	
	'''		
	
	with xlrd.open_workbook('../archive/external-data.xls') as xls_data:
		sheet= xls_data.sheet_by_index(0)
		col_num = sheet.ncols
		row_num = sheet.nrows	
		
		for col in range(1, col_num):
			filename = sheet.cell_value(2, col).split(',')[0]
			if os.path.exists('../data/' + filename +'.csv'):
				#Some of commoditie names are same before first comma, 
				#so not to overwrite exsisting one adding text till next comma
				filename += '(' + sheet.cell_value(2, col).split(',')[1].replace('/','') + ')'
				
			with open('../data/' + filename + '.csv', 'w') as csv_file:
				csvwriter = csv.writer(csv_file)
				csvwriter.writerow(['Date','Price'])
				for row in range(4, row_num):
					if type(sheet.cell_value(row, col)) is float:
						date = datetime.date(int(sheet.cell_value(row, 0).split('M')[0]), int(sheet.cell_value(row, 0).split('M')[1]), 1)
						price = sheet.cell_value(row, col)
						csvwriter.writerow([date,price])		
	
if __name__ == '__main__':
	setup()
	retrieve(source)
	process()
