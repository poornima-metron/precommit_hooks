username = ''
password = ''

# This line should be allowed because it sets the 'word' variable to an empty string
word = ""

# These lines should be blocked by the pre-commit hook because they set the 'username' and 'password' variables to
# non-empty strings
username = 'abc'
password = 'abcd'

