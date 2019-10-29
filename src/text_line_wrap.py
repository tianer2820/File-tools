# encoding=utf-8
"""
Add linebreaks every 36 chars
"""

text = ''
while True:
    i = input()
    if i == '':
        break
    else:
        text += i + '\n'

count = 0
out = ''
for c in text:
    if c == '\n':
        count = 0
    else:
        count += 1
    if count > 36:
        out += '\n'
        out += c
        count = 0
    else:
        out += c

print(out)
