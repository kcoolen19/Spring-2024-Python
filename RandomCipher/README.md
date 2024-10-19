# Problem Details

Specifically write a script that generates a random mapping from the lower case letters to themselves. This is an encrpytion mapping that replaces each letter with the mapped element. <br />

For example if the mapping specifies that ('a','g'), all instances of 'a' go to 'g'. This to be done randomly and automatically using the random module (i.e. every time you run the script you will get a different mapping rule). <br />

Then create a dictionary that records the inverse mapping of the one created above. That is, given the cypher character as a key, map it to the original character. For example if the mapping specified ('a','g'), the dictionary would store 'g' as the key and 'a' as the associated value. <br />

Then using this rule/mapping, encrypt the string msg below (print the contents to the console), and decrypt the string using the dictionary created and print the contents to the console.
