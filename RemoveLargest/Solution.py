def largest(lst):
  largest_number = 0
  for item in lst:
    if item > largest_number:
      largest_number = item
  new_lst = [s for s in lst if s != largest_number]
  return new_lst
