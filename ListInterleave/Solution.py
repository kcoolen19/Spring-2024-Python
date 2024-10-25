def list_interleave(lst_1,lst_2):
  new_lst = []
  if len(lst_1) != len(lst_2):
    raise ValueError("Lists must be the same size")
  for i in range(len(lst_1)):
    new_lst.append(interleave_str(lst_1[i],lst_2[i]))
  return new_lst
