#TODO
# Loop through results and compare to player list.
# Sort into player name list.
# Output list results to spreadsheet.

import Selenium

def main():

    schedule_id = 270
    Selenium.open_auction_page(schedule_id)
    gridItemList = Selenium.fetch_gridItemList()
    Listing_list = Selenium.convert_gridItemList_to_Listing_list(gridItemList)
    Selenium.kill_driver()

if __name__ == '__main__':
    main()