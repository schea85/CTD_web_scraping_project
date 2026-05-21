# CTD_web_scraping_project - Global Weather Dataset

## Project Overview:
This project is a complete data pipeline that collects weather data from a weather website using web scraping, then cleans and transform the data, and prepares it for storage and visualization.

## Features
- 🌐 Web scraping using Selenium
- 🧹 Data cleaning with Pandas
- 💾 CSV data storage
- 📊 Interactive visualization 

## Environment Setup:
### 1.) Clone the repository onto local machine
```
git clone git@github.com:schea85/CTD_web_scraping_project.git
cd CTD_web_scraping_project
```

### 2.) Create and activate a virtual environment

</> mac users:
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

</> window users:
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Note:  Select Python Interpreter

### 3.)  Install dependencies
Once the virtual environment is activated:
```
pip install -r requirements.txt
```

▶️ How to Run the Project
### 1.)  Run the web scraper
```
python weather_web_scrape.py
```

### 2.). Clean and transform the data
```
python weather_data_cleaning.py
```

## Tools Used
- Python
- Selenium
- Pandas
- NumPy
- ChromeDriver/WebDriver Manager

👤 Author
Sumna Chea
GitHub: https://github.com/schea85
Email: sumnachea85@gmail.com