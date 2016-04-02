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
	if not os.path.exists('archive'):
		os.mkdir('archive')

def retrieve(source):
	'''Downloades xls data to archive directory
	
	'''
	urllib.urlretrieve(source,'archive/external-data.xls')

def process():
	'''Gets the data from xls file and puts them in seperete csv files for each comoditie
	
	'''		
	
	with open('header.csv', 'r') as csv_data:
		csv_reader = csv.reader(csv_data)
		for line in csv_reader:
			header = line
	with xlrd.open_workbook('archive/external-data.xls') as xls_data:
		sheet= xls_data.sheet_by_index(0)
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
