Implement a scrabble predicate function that takes two parameters: a set of characters (a string) and a word, and checks whether the given set can be used to create the word. The function returns True or False as a result of the call. The check takes into account the number of characters needed to create the word, and does not take their case into account. Use the built-in tool Counter to solve this.

Example:
>>> scrabble('rkqodlw', 'world')
True
>>›> scrabble('avj', 'java')
False
›>> scrabble('avjafff', 'java')
True
>>> scrabble('', 'hexlet')
False
>>> scrabble('scriptingjava', 'JavaScript')
True