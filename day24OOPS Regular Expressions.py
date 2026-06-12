'''
Regular Expressions:-(RegEx):
-->RegEx is a sequence of characters that form a searching pattern.......
-->This can be used to check if a string contain the specified search pattern
-->Python has a built-in package called 're' which can be used to work with RegEx...
Functions in RegularExpression:-
1.Fimdall
2.Search
3.fullmatch

Metacharacters:-
1.[]:a-z,A-Z,0-9 and any specified sequence......

import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.search('[alds]',any_))

import re
any_ = "Python is a high-level, general purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('[a-z]',any_))

import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('[0-5]',any_))


2. .
-->here each dot is one char
import re
any_ = "Python is a high-level, general purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.search('pu....e',any_))

import re
any_ = "Python is a high-level, general purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('pu....e',any_))

3. ^ cap symbol:this look for the,string is starting with specified sequence or not...
ex:
import re
any_ = "Python is a high-level, general purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('Python',any_))

import re
any_ = "Python is a high-level, general purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.search('Python',any_))

4.$-->This looks for the ,string is ending with specified sequence or not....
import re
any_ = "Python is a high-level, general purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('onal$',any_))

import re
any_ = "Python is a foundational"
print(re.findall('onal$',any_))

5.*-->Zero or more

import re
any_ = "Python is a foundational"
print(re.search('P.*thon',any_))

import re
any_ = "Python is a foundational"
print(re.findall('P.*thon',any_))

6.?-->Zero or one

ex:
import re
any_ = "Python is a foundational"
print(re.findall('P.?thon',any_))

import re
any_ = "Python is a foundational"
print(re.search('P.?thon',any_))

7. +-->one or more
import re
any_ = "Python is a foundational"
print(re.findall('P.+ython',any_))

8. {}-->

ex:
import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('P.{16}',any_))

9.Special Sequence (\S): it will give the whole output without spaces.
EX:
import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('\S',any_))
/s:it will not give only spaces
import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('\s',any_))
10. D :it will give non digits.
import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('\D',any_))

d:it will give only digits
import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('\d',any_))

11. \w : only underscores and digits
import re
any_ = "Python is a high-level, general-purpose programming language known for its emphasis on code readability and simplicity.  Designed by Guido van Rossum and first released in 1991, it uses significant indentation and  syntax to make coding accessible to beginners while remaining powerful for experts."
print(re.findall('\w',any_))

\W :it will give non words
'''
import re
mobile_ = input("Enter 10 digit mobile num:")
sow = re.fullmatch('[6-9][0-9]{9}',mobile_)
if sow:
    print(f"{mobile_}this is a Indian number")
else:
    print(f"{mobile_}this is not Indian number")













































































