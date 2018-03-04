import sys

checksum1 = input("Bitte zur Verfügung gestellte Checksum eingeben: ")
checksum2 = input("Bitte selbst ermittelte Checksum eingeben: ")

if checksum1 == checksum2:
    print("OK")
else:
    print("NOK")
    