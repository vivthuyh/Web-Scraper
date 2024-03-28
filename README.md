# Web-Scraper
Yahoo Stock Price Webscraper

Stock Price Web Scraper with Flask

This project is a simple web application built with Flask that allows users to retrieve real-time stock prices from Yahoo Finance. Users can input the stock symbols they are interested in, and the application will display the current price, change, and percent change for each stock.

Features:
- Web Scraping: Utilizes BeautifulSoup and requests libraries to scrape data from Yahoo Finance.
- Dynamic User Input: Users can input stock symbols through a form on the web interface.
- Real-Time Data: Retrieves real-time stock data, including price, change, and percent change.
- Simple Interface: Displays the scraped data in a tabular format for easy visualization.

Technologies Used:
- Python
- Flask
- BeautifulSoup
- Pandas
  
How to Use:
- Clone the repository to your local machine.
- Install the required dependencies by running pip install -r requirements.txt.
- Run the Flask application by executing python app.py in the terminal.
- Access the application by navigating to http://127.0.0.1:5000 in your web browser.
- Enter the stock symbols you want to see in the input form and submit the form.
- View the real-time stock data displayed on the webpage.

Future Enhancements:
- Add error handling for invalid input.
- Improve the user interface with additional styling.
- Implement user authentication and save user preferences.
