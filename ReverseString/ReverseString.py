def reverse_string(word):
  # Variable that will store the word written in reverse
  new_word = ""
  # For loop to check each character of the word in the parameter from the last to the first one
  for i in range(len(word)-1,0,-1):
    # Each letter is added until the second letter is reached
    new_word = new_word + word[i]
  # The first letter is then added in the end 
  new_word += word[0]
  # The reverse word is printed
  print(new_word)

# Output = "nohtyp"
reverse_string("python")
