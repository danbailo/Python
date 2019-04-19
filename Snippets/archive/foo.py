#duplica um arquivo

with open("infile.txt") as in_f:
    with open("out.txt", "w") as out_f:
        for line in in_f:
            out_f.write(line)
