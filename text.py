def revword(word):
    word = word.lower()
    return word[::-1]

fname = 'text.txt'

def countword(fname):
    fh = open(fname, "r")
    first_word = fh.read()
    first_word = first_word.split()[0]
    count = 1
    with open(fname, 'r') as a_file:
        for line in a_file:
            if line.startswith(first_word):
                continue
            for w in line.split():
                w_new = revword(w)
                if w_new == first_word:
                    count += 1

    return count

