from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

# Web Scraping

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://www.timeanddate.com/weather/")
    print(driver.title)
    table = driver.find_element(By.CSS_SELECTOR, "table[class='zebra fw tb-theme']")
    data_info = []
    if table:
        table_body = table.find_element(By.TAG_NAME, "tbody")
        if table_body:
            table_rows = table_body.find_elements(By.TAG_NAME, "tr")
            for row in table_rows:
                city_datas = row.find_elements(By.TAG_NAME, "td")
                
                # slice 
                city_column_1 = city_datas[0:4]
                city_column_2 = city_datas[4:8]
                city_column_3 = city_datas[8:12]
                
                # extract data city column 1
                city_column_1_name = city_column_1[0].text.strip()
                city_column_1_time = city_column_1[1].text.strip()
                city_column_1_description = city_column_1[2].find_element(By.TAG_NAME, "img").get_attribute("title")
                city_column_1_temperature = city_column_1[3].text.strip()
                
                # extract data city column 2
                city_column_2_name = city_column_2[0].text.strip()
                city_column_2_time = city_column_2[1].text.strip()
                city_column_2_description = city_column_2[2].find_element(By.TAG_NAME, "img").get_attribute("title")
                city_column_2_temperature = city_column_2[3].text.strip()
                
                # extract data city column 3
                city_column_3_name = city_column_3[0].text.strip()
                city_column_3_time = city_column_3[1].text.strip()        
                city_column_3_description = city_column_3[2].find_element(By.TAG_NAME, "img").get_attribute("title")
                city_column_3_temperature = city_column_3[3].text.strip()
                
                data_info.append({"City": city_column_1_name, "Time": city_column_1_time, "Weather Description": city_column_1_description, "Temperature": city_column_1_temperature})
                data_info.append({"City": city_column_2_name, "Time": city_column_2_time, "Weather Description": city_column_2_description, "Temperature": city_column_2_temperature})
                data_info.append({"City": city_column_3_name, "Time": city_column_3_time, "Weather Description": city_column_3_description, "Temperature": city_column_3_temperature})
           
           
except Exception as e:
    print(f"Could not get data. {e}")
finally:
    driver.quit()
    
# Create DF to CSV
weather_df = pd.DataFrame(data_info)
weather_df.to_csv("weather_data_raw.csv", index=False)