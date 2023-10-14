import csv

def intro():
  print("Welcome to the English to Spanish and French translator app!\nPlease enter an English word and press the 'Enter' key.\n")
  print("Enter 'done' at any time to exit the app.\n")

def exit():
  print("\nThanks for using the translator app. Have a wonderful day!\n")
  
translations = {}

with open("translations.csv", "r") as words:
  reader = csv.DictReader(words, delimiter=",")
  for line in reader:
    english = line["English"].lower()
    spanish = line["Spanish"].lower()
    french = line["French"].lower()
    translations[english] = [spanish,french]

done = False

intro()

while not done:
  word = input("Type an English word to translate:\n")
  word = word.lower()

  if word == "done":
    done = True
    exit()
  elif word in translations:
    print(f"\nSPANISH:{translations[word][0]}")
    print(f"\nFRENCH:{translations[word][1]}\n")
  else:
    print("\nTranslation not found")
    