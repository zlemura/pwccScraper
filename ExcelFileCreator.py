#https://xlsxwriter.readthedocs.io/working_with_cell_notation.html

import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
from datetime import datetime
import pandas as pd
import os.path

def create_excel_file(schedule_id):
    formatted_datetime = datetime.now().strftime("%Y-%m-%d")
    workbook_name = 'PWCC_' + str(schedule_id) + '_listing_summary_' + formatted_datetime + '.xlsx'

    #Check if file exists and delete if so.
    if os.path.isfile(workbook_name):
        os.remove(workbook_name)

    writer = pd.ExcelWriter(workbook_name, engine='xlsxwriter')

    workbook = writer.book
    worksheet = workbook.add_worksheet()

    return workbook, worksheet, writer

def add_column_headers(workbook, worksheet, writer):
    worksheet.write(0, 0, 'Full Name')
    worksheet.write(0, 1, 'First Name')
    worksheet.write(0, 2, 'Last Name')
    worksheet.write(0, 3, 'Nickname')
    worksheet.write(0, 4, 'Listing Title')
    worksheet.write(0, 5, 'Listing URL')

    return workbook, worksheet, writer

def test_method():
    row = 1
    col = 0
    print()

def add_summarised_data_to_worksheet(workbook, worksheet, writer, summarised_Listing_list, filtered_Listing_list):
    row = 1
    players_added_to_worksheet = []

    for key in summarised_Listing_list:
        key_value = summarised_Listing_list[key]
        for listing in filtered_Listing_list:
            if listing.matched_Player == key:
                #if listing.matched_Player not in players_added_to_worksheet:
                players_added_to_worksheet.append(listing.matched_Player)
                #formula = "=_xlfn.CONCAT(_xlfn.CONCAT((" + xl_rowcol_to_cell(row, 1) + ",' '), " + xl_rowcol_to_cell(row, 2) + ")"
                #Working in excel - =TRIM(CONCAT(CONCAT(B2, " "), C2))
                #Working in python with static values - formula = "TRIM(_xlfn.CONCAT(_xlfn.CONCAT(B2, " "), C2))"
                formula = 'TRIM(_xlfn.CONCAT(_xlfn.CONCAT(' + xl_rowcol_to_cell(row, 1) + ', " "), ' + xl_rowcol_to_cell(row, 2) + '))'
                worksheet.write_formula(xl_rowcol_to_cell(row,0) , formula)
                worksheet.write(xl_rowcol_to_cell(row, 1), str(listing.matched_Player.first_name))
                worksheet.write(xl_rowcol_to_cell(row, 2), str(listing.matched_Player.last_name))
                worksheet.write(xl_rowcol_to_cell(row, 3), str(listing.matched_Player.nick_name))
                players_added_to_worksheet.append(listing.matched_Player)
                worksheet.write(xl_rowcol_to_cell(row, 4), listing.title)
                worksheet.write(xl_rowcol_to_cell(row, 5), listing.url)
                row += 1

    return workbook, worksheet, writer

def close_workbook(workbook):
    workbook.close()
