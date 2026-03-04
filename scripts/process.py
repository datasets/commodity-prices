#!/usr/bin/python3
# -*- coding: utf8 -*-

import os
from urllib import request
import datetime
import csv
import pandas as pd


source = "http://www.imf.org/external/np/res/commod/External_Data.xls"
source2 = "https://www.imf.org/-/media/Files/Research/CommodityPrices/Monthly/external-data.ashx"  # Your new source


def setup():
    """Creates the directories for archive and data if they don't exist"""
    if not os.path.exists("archive"):
        os.mkdir("archive")
    if not os.path.exists("data"):
        os.mkdir("data")


def retrieve(source, filename):
    """Downloads xls data to archive directory"""
    request.urlretrieve(source, f"archive/{filename}")


def parse_period(value):
    text = str(value).strip()
    if not text or text.lower() == "nan":
        return None
    if "M" in text:
        year, month = text.split("M", 1)
        try:
            return datetime.date(int(year), int(month), 1)
        except ValueError:
            return None
    try:
        dt = pd.to_datetime(text)
        return datetime.date(dt.year, dt.month, 1)
    except Exception:
        return None


def process_data(input_file, output_file):
    """Gets the data from xls file and puts them in separate csv files for each commodity"""

    header = [
        "Date",
        "All Commodity Price Index",
        "Non-Fuel Price Index",
        "Food and Beverage Price Index",
        "Food Price Index",
        "Beverage Price Index",
        "Industrial Inputs Price Index",
        "Agricultural Raw Materials Index",
        "Metals Price Index",
        "Fuel Energy Index",
        "Crude Oil petroleum",
        "Aluminum",
        "Bananas",
        "Barley",
        "Beef",
        "Coal",
        "Cocoa beans",
        "Coffee Other Mild Arabicas",
        "Coffee Robusta",
        "Rapeseed oil",
        "Copper",
        "Cotton",
        "Fishmeal",
        "Groundnuts peanuts",
        "Hides",
        "China import Iron Ore Fines 62% FE spot",
        "Lamb",
        "Lead",
        "Soft Logs",
        "Hard Logs",
        "Maize corn",
        "Natural Gas - Russian Natural Gas border price in Germany",
        "Natural Gas - Indonesian Liquefied Natural Gas in Japan",
        "Natural Gas - Spot price at the Henry Hub terminal in Louisiana",
        "Nickel",
        "Crude Oil - petroleum-simple average of three spot prices",
        "Crude Oil - petroleum - Dated Brent light blend",
        "Oil Dubai",
        "Crude Oil petroleum - West Texas Intermediate 40 API",
        "Olive Oil",
        "Oranges",
        "Palm oil",
        "Swine - pork",
        "Poultry chicken",
        "Rice",
        "Rubber",
        "Fish salmon",
        "Hard Sawnwood",
        "Soft Sawnwood",
        "Shrimp",
        "Soybean Meal",
        "Soybean Oil",
        "Soybeans",
        "Sugar European import price",
        "Sugar Free Market",
        "Sugar U.S. import price",
        "Sunflower oil",
        "Tea",
        "Tin",
        "Uranium",
        "Wheat",
        "Wool coarse",
        "Wool fine",
        "Zinc",
    ]

    df = pd.read_excel(f"archive/{input_file}", sheet_name=0)
    with open(f"data/{output_file}", "w", newline="") as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(header)
        for _, row in df.iloc[4:].iterrows():
            parsed_date = parse_period(row.iloc[0])
            if not parsed_date:
                continue
            csv_row = [parsed_date]
            for price in row.iloc[1:]:
                csv_row.append(price)
            csvwriter.writerow(csv_row)


def process(data_src, archive_file, output_file):
    try:
        retrieve(data_src, archive_file)
        process_data(archive_file, output_file)
    except Exception as exc:
        print(f"Failed processing {archive_file} from {data_src}: {exc}")


if __name__ == "__main__":
    setup()
    process(source, "external-data.xls", "commodity-prices.csv")
    process(source2, "external-data-v2.xls", "commodity-prices_v2.csv")
