import re

print("=== ПРАКТИКА 5: ПРИМЕРЫ REGEX (W3SCHOOLS) ===\n")

text = "The rain in Spain falls mainly in the plain! 123-456. Hello World."

print("1. search() (найти 'Spain'):", re.search(r"Spain", text).group())

print("2. findall() (все 'ain'):", re.findall(r"ain", text))

print("3. split() (разрезать по пробелам):", re.split(r"\s", "Hello World"))

print("4. sub() (замена пробелов на '_'):", re.sub(r"\s", "_", "Hello World"))

print("5. match() (начинается с 'The'?):", bool(re.match(r"The", text)))

print("6. Метасимволы (^ и $ - начало/конец):", bool(re.search(r"^The.*World\.$", text)))

print("7. Спец. последовательности (\\d - цифры):", re.findall(r"\d", text))

print("8. Sets [a-c] (найти a, b, c):", re.findall(r"[abc]", text))

print("9. Квантификаторы (\\d{3} - три цифры подряд):", re.findall(r"\d{3}", text))

print("10. Флаги (IGNORECASE на 'the'):", re.findall(r"the", text, re.IGNORECASE))
