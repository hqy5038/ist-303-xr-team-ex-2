# Concurrency example using multiple implementations
# Example searches for a topic on wikipedia, gets related topics and 
#   saves the references from related topics in their own text file
# info on wikipedia library: https://thepythoncode.com/article/access-wikipedia-python
# info on concurrent.futures library: https://docs.python.org/3/library/concurrent.futures.html#

import time
import wikipedia
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

#convert objects produced by wikipedia package to a string var for saving to text file
def convert_to_str(obj):
  if type(obj) == list:
    mystr = '\n'.join(obj)
    return mystr
  elif type(obj) in [str, int, float]:
    return str(obj)

# IMPLEMENTATION 1: sequential example
def wiki_sequentially():
  t_start = time.perf_counter()
  results = wikipedia.search("general artificial intelligence")
  
  def dl_and_save(item):
    page = wikipedia.page(item, auto_suggest=False)
    title = page.title
    references = convert_to_str(page.references)
    out_filename = title + ".txt"
    with open(out_filename, 'wt') as fileobj:
      fileobj.write(references)

  for item in results:
    dl_and_save(item)

  print('\nsequential function:')

  t_end = time.perf_counter()
  t_lapse = t_end - t_start
  print(f'code executed in {t_lapse} seconds')

# IMPLEMENTATION 2: concurrent example w/ threads
def concurrent_threads():
  t_start = time.perf_counter()
  results = wikipedia.search("general artificial intelligence")
  
  def dl_and_save_thread(item):
    page = wikipedia.page(item, auto_suggest=False)
    title = page.title
    references = convert_to_str(page.references)
    out_filename = title + ".txt"
    with open(out_filename, 'wt') as fileobj:
      fileobj.write(references)

  with ThreadPoolExecutor() as executor:
    executor.map(dl_and_save_thread, results)
  print('\nthread pool function:')

  t_end = time.perf_counter()
  t_lapse = t_end - t_start
  print(f'code executed in {t_lapse} seconds')

# IMPLEMENTATION 3: concurrent example w/ processes
def concurrent_process():
  t_start = time.perf_counter()
  results = wikipedia.search("general artificial intelligence")
  
  def dl_and_save_process(item):
    page = wikipedia.page(item, auto_suggest=False)
    title = page.title
    references = convert_to_str(page.references)
    out_filename = title + ".txt"
    with open(out_filename, 'wt') as fileobj:
      fileobj.write(references)

  with ProcessPoolExecutor() as executor:
    executor.map(dl_and_save_process, results)
  print('\nprocess pool function:')

  t_end = time.perf_counter()
  t_lapse = t_end - t_start
  print(f'code executed in {t_lapse} seconds')

if __name__ == "__main__":
  wiki_sequentially()
  concurrent_threads()
  concurrent_process()