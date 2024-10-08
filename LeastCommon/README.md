# Problem Details <br />
Write a function least_common that takes a parameter as a dictionary, and returns the key corresponding to the lowest frequency value. In the case of ties, you may return either value.<br />

For example consider the dictionary {1:"hello", 2:"hello", 3: "hi", 4: "bye", 5: "bye"}<br />

The function should return 3, because the value "hi" only occurs once in the dictionary, whereas all other values occur more than once.<br />
Note that the key/value pairs need not be ints/strings as shown above. Please raise a ValueError() if the dictionary is empty<br />

Hint: You may consider creating an alternate dictionary with the values as keys, and the values corresponding the the value count of the original dictionary's values.<br /> For example, such a dictionary for the above example would be:<br />

{"hello":2, "hi": 1, "bye": 2}
