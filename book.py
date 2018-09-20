import re #regular expressions
import collections

text = open('book.txt').read().lower() #open file in read only and lowercase
words = re.findall('\w+', text) #find all non-whitespace 
print(collections.Counter(words).most_common(10)) #count the top 10 words