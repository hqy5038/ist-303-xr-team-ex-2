# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#

import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import os

def convert_to_str(page):
    """
    Convert the references of a Wikipedia page to a string.
    If the page has no external links ('extlinks'), return a default message.
    """
    try:
        if type(page) == list:
            return '\n'.join(page)
        elif hasattr(page, 'references'):
            references = page.references
            return '\n'.join(references)
    except KeyError:
        return "No external links available."
    except Exception as e:
        return f"An error occurred: {e}"
    return str(page)

def validate_search_term(term):
    """Validate the search term length, defaulting to 'generative artificial intelligence' if less than 4 characters."""
    return term if len(term) >= 4 else "generative artificial intelligence"

def wiki_sequentially(search_term="general artificial intelligence"):
    search_term = validate_search_term(search_term)
    t_start = time.perf_counter()
    results = wikipedia.search(search_term)
    
    resolved_results = []
    for item in results:
        try:
            page = wikipedia.page(item, auto_suggest=False)
            resolved_results.append(item)  # Item is not a disambiguation page
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"DisambiguationError for '{item}', choosing first option '{e.options[0]}'")
            resolved_results.append(e.options[0])  # Choose the first option or implement other logic

    def dl_and_save(item):
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        subfolder = "wiki_dl"
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        out_filename = os.path.join(subfolder, title + ".txt")
        with open(out_filename, 'wt') as fileobj:
            fileobj.write(references)

    for item in resolved_results:
        dl_and_save(item)

    t_end = time.perf_counter()
    print('\nsequential function:')
    print(f'code executed in {round(t_end - t_start, 1)} seconds')

def concurrent_threads(search_term="general artificial intelligence"):
    search_term = validate_search_term(search_term)
    t_start = time.perf_counter()
    results = wikipedia.search(search_term)
  
    def dl_and_save_thread(item):
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        subfolder = "wiki_dl"
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        out_filename = os.path.join(subfolder, title + ".txt")
        with open(out_filename, 'wt') as fileobj:
            fileobj.write(references)

    with ThreadPoolExecutor() as executor:
        executor.map(dl_and_save_thread, results)
    print('\nthread pool function:')
    t_end = time.perf_counter()
    print(f'code executed in {round(t_end - t_start, 1)} seconds')

def concurrent_process(search_term="general artificial intelligence"):
    search_term = validate_search_term(search_term)
    t_start = time.perf_counter()
    results = wikipedia.search(search_term)
  
    def dl_and_save_process(item):
        page = wikipedia.page(item, auto_suggest=False)
        title = page.title
        references = convert_to_str(page.references)
        subfolder = "wiki_dl"
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        out_filename = os.path.join(subfolder, title + ".txt")
        with open(out_filename, 'wt') as fileobj:
            fileobj.write(references)

    with ProcessPoolExecutor() as executor:
        executor.map(dl_and_save_process, results)
    print('\nprocess pool function:')
    t_end = time.perf_counter()
    print(f'code executed in {round(t_end - t_start, 1)} seconds')

if __name__ == "__main__":
    search_term = input("Enter search term: ")
    wiki_sequentially(search_term)
    concurrent_threads(search_term)
    concurrent_process(search_term)
