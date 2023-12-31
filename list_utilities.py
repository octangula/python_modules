# tiny useless one liners (but super speedy compared to list comprehension especially for larger lists)

from collections import OrderedDict

# similar to mathematical set difference except dedupes
def difference(list_a, list_b):
  return dedupe(list_b + list_a)[len(dedupe(list_b)):]

# super speedy dedupe by converting to dict & back
def dedupe(list_a):
  return list(OrderedDict.fromkeys(list_a))

# just.. add the lists together & dedupe
def combine(list_a, list_b):
  return dedupe(list_a + list_b)

