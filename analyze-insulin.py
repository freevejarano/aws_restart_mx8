import re

with open('preproinsulin-seq.txt', mode='r+') as file:
    cadena = "".join(file.readlines())
    preproinsulin = re.sub('ORIGIN|[0-9]|//|\n|\t|\s','', cadena)
    print(preproinsulin)
    lsinsulin = preproinsulin[0:24]
    print(lsinsulin)
    binsulin = preproinsulin[24:54]
    print(binsulin)
    cinsulin = preproinsulin[54:89]
    print(cinsulin)
    ainsulin = preproinsulin[89:110]
    print(ainsulin)

with open("lsinsulin-seq-clean.txt", mode="w") as file:
    file.write(lsinsulin)
    
with open("binsulin-seq-clean.txt", mode="w") as file:
    file.write(binsulin)
    
with open("cinsulin-seq-clean.txt", mode="w") as file:
    file.write(cinsulin)

with open("ainsulin-seq-clean.txt", mode="w") as file:
    file.write(ainsulin)