#TODO
# Create logic to write player record to worksheet.
# Loop through and add listings to worksheet.

import xlsxwriter
from datetime import datetime

def create_excel_file(schedule_id):
    formatted_datetime = datetime.now().strftime("%Y-%m-%d")
    workbook_name = 'PWCC_' + str(schedule_id) + '_listing_summary_' + formatted_datetime + '.xlsx'
    workbook = xlsxwriter.Workbook(workbook_name)
    worksheet = workbook.add_worksheet()

    return workbook, worksheet

def add_column_headers(workbook, worksheet):
    worksheet.write(0, 0, 'Full Name')
    worksheet.write(0, 1, 'First Name')
    worksheet.write(0, 2, 'Last Name')
    worksheet.write(0, 3, 'Nickname')
    worksheet.write(0, 4, 'Listing Title')
    worksheet.write(0, 4, 'Listing URL')

    return workbook, worksheet

def add_summarised_data_to_worksheet(workbook, worksheet, summarised_Listing_list, filtered_Listing_list):
    row = 1
    col = 0
    players_added_to_worksheet = []

    for key in summarised_Listing_list:
        key_value = summarised_Listing_list[key]
        for listing in filtered_Listing_list:
            if listing.matched_Player == key:
                if listing.matched_Player not in players_added_to_worksheet:
                    players_added_to_worksheet.append(listing.matched_Player)
                    worksheet.write



    return workbook, worksheet
