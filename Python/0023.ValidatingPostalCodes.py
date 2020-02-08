regex_integer_in_range = r"\b([1-8][0-9]{5}|9[0-8][0-9]{4}|99[0-8][0-9]{3}|999[0-8][0-9]{2}|9999[0-8][0-9]|99999[0-9])\b"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

import re
P = "4542867"
integerInRange = bool(re.match(regex_integer_in_range, P))
alternatingRepetitiveDigit = len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
print(integerInRange)
print(alternatingRepetitiveDigit)
print (integerInRange & alternatingRepetitiveDigit)