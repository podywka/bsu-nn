def countWords(string):
    return string.count(" ") + 1

def replaceWords(string):
    return " ".join(reversed(string.split()))

def replaceTo(string):
    return string.replace("1", "one")

print("Words count:", countWords("London is the capital of Great Britain"))

print("Replaced words:", replaceWords("first word"))

print("Replaced 1 to one:", replaceTo("1 1 1 1 1 1 1 1 1 1"))
