# tweetWithRegex
Our aim is to structure unstructed sloppy tweets using regular expression tools and make them more readable. Thus, both individuals can read tweets more comfortably; In addition, the tweets we obtain become more suitable for automatic analysis (such as emotion analysis) with computers.
This program does the following;
  • Clean the hashtags (#).
  • Clean the ments (@).
  • If there is a lot of space between two words (if space is pressed more than once), make them one space.
  • In some places, _ is used instead of spaces, find these places and replace them with spaces.
  • Find the word between the quotation marks given in the 12th tweet and print it with print. (that is, write a regular    expression that will capture that word, pull the phrase you have captured and print it with print).
  • Clear all punctuation marks.
  • Make all capital letters lowercase.
  • If the words that should be separated in a tweet are not separated between them, separate these words with a space. As an example (for example, in tweet 3, there are structures such as Beauty Do not love, rejoice, such as Gunaydin, these structures will be as follows: Do not like beauty, rejoice Gunaydin.
  • If any letter in a word is written more than once in the tweet, make this block of letters a single letter. For example, the word Gulummm in the 17th Tweet will be Gulum, or bread in the 6th Tweet will be bread.
  • Save the cleaned tweets by printing them back into a txt file. This will be one of your assignment outputs.
  • In all tweets:
- 5 length words
words in z
- all the numbers
find, save and save to a txt file.
