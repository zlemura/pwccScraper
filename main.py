import ExcelFileCreator
import Listing
import ListingSorter
import PlayerList
import Selenium

import random
import time


def main():

    schedule_id = 270
    driver = Selenium.open_auction_page(schedule_id)
    page_limit = Selenium.determine_page_limit(driver)
    player_list = PlayerList.fetch_player_list()
    filtered_Listing_list = []
    debug_pages_to_scan = 5
    for page in range(1, debug_pages_to_scan + 1):
    #for page in range(1, page_limit+1):
        print("Processing page " + str(page) + " of " + str(page_limit))
        #Open auction page
        driver = Selenium.update_auction_page(driver, page, schedule_id)
        #Get gridItemList from page.
        gridItemList = Selenium.fetch_gridItemList(driver)
        #Convert gridItemList from page to Listing_list.
        Listing_list = Selenium.convert_gridItemList_to_Listing_list(gridItemList)
        #Filter Listing_list by player_name_list.
        for listing in Listing_list:
            #Determine if Listing.title contains any player names.
            match_method, matched_Player = ListingSorter.determine_if_listing_contains_player_name(listing, player_list)
            if match_method != '':
                listing.update_match_method(match_method)
                listing.update_matched_Player(matched_Player)
                filtered_Listing_list.append(listing)
                print(listing.title)
                print("Added listing to filtered list!")
        pause_interval = random.randint(2,5)
        print("Sleeping for " + str(pause_interval) + " seconds.")
        time.sleep(pause_interval)
        print("Finished processing page " + str(page) + " of " + str(page_limit))

    print("Final filtered listing size is " + str(len(filtered_Listing_list)))

    #Summarise listings.
    summarised_Listing_list = ListingSorter.summarise_Listing_list(filtered_Listing_list)

    #Create excel file.
    excel_workbook, excel_worksheet, excel_writer = ExcelFileCreator.create_excel_file(schedule_id)
    excel_workbook, excel_worksheet, excel_writer = ExcelFileCreator.add_column_headers(excel_workbook, excel_worksheet, excel_writer)
    excel_workbook, excel_worksheet, excel_writer = ExcelFileCreator.add_summarised_data_to_worksheet(excel_workbook, excel_worksheet, excel_writer,
                                                                                        summarised_Listing_list, filtered_Listing_list)
    ExcelFileCreator.close_workbook(excel_workbook)

    Selenium.kill_driver(driver)

if __name__ == '__main__':
    main()