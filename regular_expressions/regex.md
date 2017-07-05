# Regular Expressions

### Python 're' module

- To use regular expressions, import module 're'
```
import re
```
- re.findall()
- re.split()


### Identifiers:

- \d any number
- \D anything but a number
- \s space
- \S anything but a space
- \w any character
- \W anything but a character
- . is any character, except for a new line
- \b the white space around words
- \. a period


### Modifiers:

- {1,3} One to Three Digits (can be any range of digits) i.e. \d{1-3}
- + Match 1 or more
- ? Match 0 or 1
- * Match 0 or more
- $ Match the end of a string
- ^ Match the beginning of a string
- | either/or
- [] range or variance i.e. [A-Z]
- {x} expecting 'x' amount of characters


### White Space Characters

- \n new line
- \s space
- \t tab
- \e escape
- \f form feed
- \r return


### Additional Info

- .,+,*,?,[],$,^,(),{},|,\ all have to be escaped.