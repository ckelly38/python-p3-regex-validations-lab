import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"[A-Z][a-z]*\s[A-Z][a-z]*|[A-Z]\'[A-Z][a-z].*|[A-Z][a-z]*\s[A-Z][a-z]*-[A-Z][a-z]*"
name_regex = re.compile(name)

phone_number = r"[0-9]{10}|[0-9]{3}-[0-9]{3}-[0-9]{4}|\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"[A-z][A-z0-9._]*@[A-z]*\.[A-z]*"
email_regex = re.compile(email_address)
