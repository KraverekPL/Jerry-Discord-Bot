import requests
from bs4 import BeautifulSoup
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

