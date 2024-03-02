import requests
from bs4 import BeautifulSoup
from __main__ import logging
import random


def fibonacci_sequence(number):  # write fibonacci sequence up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    result = ''
    while a < number:
        result = result + ' ' + str(a)
        a, b = b, a + b
    return result


def random_quote_generator():
    """Displays popular quotes from the game show One of Ten"""
    try:
        url = 'https://nonsa.pl/wiki/Cytaty:Jeden_z_dziesi%C4%99ciu'
        logging.info(f'Loading data for quates from {url}')
        allQuotes = []
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        patterItems = soup.find_all('li')
        for li in patterItems:
            italics = li.find('i')
            if italics:
                allQuotes.append('\n'.join(italics.stripped_strings))

        return random.choice(allQuotes) if allQuotes else "No quotes found."
    except Exception as e:
        return f'Exception during fetching quotes {e}'


def random_tree_generator_url(url, class_parm):
    url = str(url)
    logging.info(f'Loading tree images from {url}')
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        image_elements = soup.find_all('img', class_=str(class_parm))
        random_img_element = random.choice(image_elements) if image_elements else None
        image_url = random_img_element['src']
        return image_url
    except requests.RequestException as e:
        return f'Exception during fetching quotes {e}'
