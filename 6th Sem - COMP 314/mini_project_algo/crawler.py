"""Scraper"""

from datetime import datetime
import requests
from bs4 import BeautifulSoup


class QueueError(Exception):
    """Custom Exception Decleration"""

    pass


class Queue:
    """Array implementation of queue"""

    def __init__(self):
        """Initialize queue"""
        self._data = []
        self._size = 0

    def __repr__(self):
        """String representation for Queue class"""
        return "Queue()"

    def __len__(self):
        """Returns the number of elements in Queue"""
        return self._size

    def is_empty(self):
        """Retruns true if no elements in queue else false"""
        return self._size == 0

    def peek(self):
        """Returns the element at the front of the queue."""
        if self._size == 0:
            raise QueueError("Queue underflow.")
        return self._data[0]

    def enqueue(self, item):
        """Adds an element to the end of the queue."""
        self._data.append(item)
        self._size += 1

    def dequeue(self):
        """Removes and returns the element at the front of the queue."""
        if self._size == 0:
            raise QueueError("Queue underflow.")
        retval = self._data.pop(0)
        self._size -= 1
        return retval


if __name__ == "__main__":

    headlines = []  # scraped headlines
    visited = []  # visited urls

    seed_url = "https://www.kathmandupost.com"

    to_visit = Queue()  # create queue instance
    to_visit.enqueue(seed_url)  # add base url to queue for crawling
    next = to_visit.peek()

    # crawl base page for categories
    response = requests.get(next)
    soup = BeautifulSoup(response.content, "lxml")
    sidenav = soup.find_all("div", class_="offcanvas")[0].select("a.menu-item")[:16]
    for entry in sidenav:
        to_visit.enqueue(seed_url + entry.get("href"))
    visited.append(to_visit.dequeue())  # dequeue the crawled base seed page

    # crawl categories for subcategories or scrape headlines
    while not to_visit.is_empty():
        next = to_visit.peek()
        response = requests.get(next)
        soup = BeautifulSoup(response.content, "lxml")
        subcat = soup.find("ul", class_="list-inline list-category")

        # crawl and scrape for Headlines
        if subcat is None:
            print(f"On page {next}. No subcategories found. Scraping headlines...")
            for article in soup.find_all("article")[:15]:
                headline = article.h3
                if headline is not None:
                    headlines.append(headline.get_text())

        # crawl and scrape subcategories
        else:
            print(f"On page {next}. Categories found so scraping further...")
            for entry in subcat.find_all("a"):
                if seed_url + entry.get("href") not in visited:
                    to_visit.enqueue(seed_url + entry.get("href"))

        visited.append(to_visit.dequeue())

    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_file = f"headlines_{timestamp}"
    with open(output_file, "w") as file:
        for headline in headlines:
            file.write(headline + "\n")
