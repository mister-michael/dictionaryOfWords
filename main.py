word_definitions = dict()

word_definitions["apple"] = "A red fruit."
word_definitions["bus"] = "A yellow vehicle."
word_definitions["bee"] = "A black and yellow bug."
word_definitions["bluebird"] = "A blue bird."
word_definitions["sun"] = "A red star."

print(word_definitions["apple"], word_definitions["bus"])

for word in word_definitions:
    print(f'The definition of {word} is "{word_definitions[word]}"')
 