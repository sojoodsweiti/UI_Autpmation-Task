import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r'C:\Users\almokhtar\PycharmProjects\UI_Autpmation-Task\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://www.aircanada.com/ca/en/aco/home.html")


def test_hotel_search():
    # Click on the "Hotels" tab
    hotels_tab = driver.find_element(By.XPATH, '//*[@id="bkmg-tab-button-hotels"]/abc-ripple/div')
    hotels_tab.click()

    # Select the number of guests and rooms
    guests_rooms = driver.find_element(By.XPATH, '// *[ @ id = "abcFormFieldElement71MainContainer"] / div')
    guests_rooms.click()
    # Save the result of guests and rooms
    save = driver.find_element(By.XPATH, '// *[ @ id = "abcFormFieldElement71RoomSelectorDialogButton0"] / abc - ripple / div')
    save.click()

    # Enter the location
    location_input = driver.find_element(By.NAME, "hotelsTabLocation")
    location_input.send_keys("Toronto")
    # Select the result of the location
    result = driver.find_element(By.XPATH, '// *[ @ id = "hotelsTab_locationSearchResult0"] / abc - ripple / div')
    result.click()

    # Select check-in and check-out dates
    check_in_date = driver.find_element(By.ID, "hotelsTab_checkInDates-formfield-1")
    check_in_date.send_keys("2023-05-20")
    check_out_date = driver.find_element(By.ID, "hotelsTab_checkInDates-formfield-2")
    check_out_date.send_keys("2023-05-25")

    # Click on search button
    search = driver.find_element(By.XPATH, '//*[@id="abcButtonElement74"]/abc-ripple/div')
    search.click()
    # Wait for search results to load
    driver.implicitly_wait(10)


def test_flights_search():
    # Click on the "Flights" tab
    flights_tab = driver.find_element(By.XPATH, '//*[@id="bkmg-tab-button-flight"]/abc-ripple/div')
    flights_tab.click()

    origin_input = driver.find_element(By.ID, "bkmgFlights_origin_trip_1")
    origin_input.send_keys("Toronto")
    origin_result = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_origin_trip_1SearchResult0"]/abc-ripple/div')
    origin_result.click()

    destination_input = driver.find_element(By.ID, "bkmgFlights_destination_trip_1")
    destination_input.send_keys("Vancouver")
    destination_result = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_destination_trip_1SearchResult1"]/abc-ripple/div')
    destination_result.click()

    # Select the departure and return dates
    departure_date = driver.find_element(By.ID, "bkmgFlights_travelDates_1-formfield-1")
    departure_date.send_keys("2023-05-20")

    return_date = driver.find_element(By.ID, "bkmgFlights_travelDates_1-formfield-2")
    return_date.send_keys("2023-05-25")

    passengers = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_selectTravelersMainContainer"]/div')
    passengers.click()
    close_button = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_selectTravelers_confirmTravelers"]/abc-ripple/div')
    close_button.click()

    # Click on the search button
    search_button = driver.find_element(By.XPATH, '//*[@id="bkmgFlights_findButton"]/abc-ripple/div')
    search_button.click()

    # Wait for search results to load
    driver.implicitly_wait(10)


def test_search_bar():
    # Find the search input field
    search_input = driver.find_element(By.ID, "acSiteSearchInput")

    # Enter a keyword
    search_input.send_keys("Toronto")

    # Click on the search button
    search_button = driver.find_element(By.XPATH, '//*[@id="pageHeader"]/div[1]/div/div/div[3]/ngx-ac-site-search/form/abc-input/abc-form-element-container/div/div/div/abc-affix/div/button')
    search_button.click()

    # Wait for search results to load
    driver.implicitly_wait(10)







