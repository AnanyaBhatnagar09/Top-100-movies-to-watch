# Top-100-movies-to-watch
This Python script scrapes a list of the top movies from a specific webpage and saves the titles into a text file. The webpage used for this script is an archived version of Empire Online's "Best Movies" list.

Features

Web Scraping: Utilizes the requests library to fetch the HTML content of the webpage.
HTML Parsing: Employs BeautifulSoup to parse the HTML and extract movie titles.
Data Handling: Reverses the order of the movie titles to match the original ranking (from 1 to 100).
File Writing: Writes the list of movie titles into a text file named movies.txt.
Libraries Used

requests: To make an HTTP request to the webpage.
BeautifulSoup (from bs4): To parse and navigate the HTML content.
How It Works

Fetch HTML Content: The script sends a GET request to the specified URL and retrieves the HTML content of the webpage.
Parse HTML: Using BeautifulSoup, the script parses the HTML to find all elements that match the specified tag and class (<h3> tags with the class title).
Extract Movie Titles: The script extracts the text content from each of these elements, which represents the movie titles.
Reverse Order: Since the webpage lists movies from 100 to 1, the script reverses the order to have them from 1 to 100.
Save to File: Finally, the script writes the movie titles into a text file, each title on a new line.
