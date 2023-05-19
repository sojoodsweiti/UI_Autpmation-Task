import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


chrome_driver_path = r'C:\Users\almokhtar\PycharmProjects\UI_Autpmation-Task\chromedriver.exe'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.get("https://www.aircanada.com/ca/en/aco/home.html")


def test_hotel_search():
    # Click on the "Hotels" tab
    hotels_tab = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmg-tab-button-hotels"]')))
    hotels_tab.click()

    # Enter the location
    location_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="hotelsTab_location"]')))
    location_input.send_keys("Toronto")

    # Select the result of the location
    #result = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hotelsTab_locationSearchResult0"]/abc-ripple/div')))
    #result.click()

    # Select check-in and check-out dates
    check_in_date = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="hotelsTab_checkInDates-formfield-1"]')))
    check_in_date.click()
    select_check_in = wait.until(EC.element_to_be_clickable((By.ID, "hotelsTab_checkInDates-date-2023-05-18")))
    select_check_in.click()
    check_out_date = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="hotelsTab_checkInDates-formfield-2"]')))
    check_out_date.click()
    select_check_in = wait.until(EC.element_to_be_clickable((By.ID, "hotelsTab_checkInDates-date-2023-05-21")))
    select_check_in.click()

    # Click on search button
    try:
        # Click on search button
        search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="abcButtonElement97"]')))
        search.click()
    except TimeoutException:
        print("Element not found within the specified timeout.")


    # Wait for search results to load
    driver.implicitly_wait(10)


def test_flights_search():
    # Click on the "Flights" tab
    flights_tab = wait.until(EC.element_to_be_clickable((By.ID, "bkmg-tab-button-flight")))
    flights_tab.click()

    # Enter the origin location
    origin_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_origin_trip_1"]')))
    origin_input.send_keys("Toronto")
    origin_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_origin_trip_1SearchResult0"]')))
    origin_result.click()

    # Enter the destination location
    destination_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_destination_trip_1"]')))
    destination_input.send_keys("Vancouver")
    destination_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_destination_trip_1SearchResult0"]')))
    destination_result.click()

    # Select the departure
    departure_date = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_travelDates_1-formfield-1"]')))
    departure_date.click()
    select_dep_date = wait.until(EC.element_to_be_clickable((By.ID, "bkmgFlights_travelDates_1-date-2023-05-18")))
    select_dep_date.click()

    # Select the return date
    return_date = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_travelDates_1-formfield-2"]')))
    return_date.click()
    select_ret_date = wait.until(EC.element_to_be_clickable((By.ID, "bkmgFlights_travelDates_1-date-2023-05-23")))
    select_ret_date.click()

    # Confirm the selected dates
    select_button = wait.until(EC.element_to_be_clickable((By.ID, "bkmgFlights_travelDates_1_confirmDates")))
    select_button.click()

    # Open the passengers selection
    passengers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_selectTravelers"]')))
    passengers.click()

    # Close the passengers selection window
    close_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_selectTravelers_confirmTravelers"]')))
    close_button.click()

    # Click on the search button
    search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="bkmgFlights_findButton"]')))
    search_button.click()

    # Wait for search results to load
    driver.implicitly_wait(10)


def main():
    # Call your test case functions here
    test_flights_search()
    test_hotel_search()


if __name__ == "__main__":
    main()



