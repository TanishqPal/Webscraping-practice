# Book Scraper

This is a Python script that scrapes book titles from the website [http://books.toscrape.com/](http://books.toscrape.com/).

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:

- Python 3.x
- Requests library: `pip install requests`
- BeautifulSoup library: `pip install beautifulsoup4`

## Usage

1. Clone the repository:

git clone <repository-url>


2. Install the required libraries:


pip install -r requirements.txt



3. Run the script:

python scrape_books.py



## Functionality

The script performs the following steps:

1. Sends a GET request to the website [http://books.toscrape.com/](http://books.toscrape.com/).
2. Retrieves the HTML content of the website.
3. Parses the HTML using BeautifulSoup.
4. Extracts book titles from the webpage.
5. Prints the titles to the console.

## Error Handling

The script includes error handling to handle potential exceptions that may occur during the scraping process. If an error occurs, an informative error message will be displayed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is not licensed
