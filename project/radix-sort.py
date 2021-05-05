import urllib
import requests

def max(data):
  max = len(str(data[0]))
  for i in range(len(data)):
    if len(str(data[i])) > max:
      max = len(str(data[i]))
  return max

def equalizeData(data, mL):
  lst = []
  for item in data:
    if isinstance(item, int):
      itemlst = list(str(item))
      lst.append(['\0'] * (mL-len(itemList)) + itemlst)
    elif isinstance(item, str):
      itemlst = list(item)
      lst.append(itemlst + ['\0'] * (mL-len(itemlst)))
  return lst

def Sort(lst, pos):
  x = []
  Size = 256
  count = [0] * Size
  buckets = [[] for _ in range(Size)]
  for i in range(len(lst)):
    buckets[ord(lst[i][pos])% Size].append(lst[i])
  return [item for bucket in buckets for item in bucket]


def radixSort(data):
  longest = max(data)
  lst = equalizeData(data, longest)
  for i in range(longest):
    lst = Sort(lst, longest-i-1)
  lst = [item.strip('\0') for item in [''.join(item) for item in lst]]
  for i in range(len(lst)):
    if isinstance(data[i], int):
      lst[i] = int(lst[i])
    elif isinstance(data[i], float):
      lst[i] = float(lst[i])
  return lst

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
  file = urllib.request.urlopen(book_url).read().decode()
  lst = [str(n)[2:-1] for n in file.encode('ascii','replace').split()]
  return radixSort(lst)

print(radix_a_book())
