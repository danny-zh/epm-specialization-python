# epm-specialization-python
A simple repo for developing katas of python challenges for the specialization devops course of epam

### DESCRIPTION

Need to succesfully implement the following three tasks:

1. In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

    ```
        d = Dictionary()

        d.newentry('Apple', 'A fruit that grows on trees')

        print(d.look('Apple'))
        #A fruit that grows on trees

        print(d.look('Banana'))
        #Can't find entry for Banana
    ```

2. How much will you spend?

    Given a dictionary of items and their costs and an array specifying the items bought, calculate the total cost of the items plus a given tax.

    If an item doesn't exist in the given cost values, the item is ignored.

    Output should be rounded to two decimal places.

    ```
        costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
        get_total(costs, ['socks', 'shoes'], 0.09)
        # -> 5 + 60 = 65
        # -> 65 + 0.09 of 65 = 70.85
        # -> Output: 70.85
    ```

3. Complete the function that takes an array of words.

    You must concatenate the nth letter from each word to construct a new word which should be returned as a string, where n is the position of the word in the list.

    For example:

    ```
        ["yoda", "best", "has"]  -->  "yes"
        ^       ^       ^
        n=0     n=1     n=2
    ```
    
    Note: Test cases contain valid input only - i.e. a string array or an empty array; and each word will have enough letters.


