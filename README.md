# Kanji Scraper
### What is this
There are two main functions of this program:
1. To take in a CSV file of containing a list of Japanese vocabulary and output a CSV file containing all the Kanji used and the RTK definitions
2. To take in a CSV file containing RTK (Remembering the Kanji) definitions and output a CSV file containing the Kanji and RTK

This exported CSV file can be imported into Anki
---

### How to run
This program runs on Python 3, so that needs to be installed
1. Make sure to download `scraper.py` and `rtk_list.csv` and make sure they're in the same folder
2. In a terminal, cd to the folder that contains the files. For example on Mac if the two files are stored in a folder called `scraper` on the Desktop, you should `cd Desktop/scraper`
3. Give the file permission to run by typing `chmod +x scraper.py`
4. Run the file by typing `python3 scraper.py`

---

### Japanese vocabulary -> Kanji + RTK definitions
A CSV file containing Japanese vocabulary should be structured as follows including headings:

NB. The English column isn't necessary but the vocabulary should be stored in the first column in rows

Japanese | English
--- | --- 
お風呂 | Bath
歌 | Song
女の人 | Woman
コンビニ | Convenience store
来週 | Next week
... | ...


1. Click Kanji -> RTK
2. Locate the CSV file containing the vocabulary and click open
3. Enter a file name and save in your desired folder

---

### RTK definitions -> Kanji + RTK definitions
A CSV file containing RTK definitions should be structured as follows:

RTK Definitions |
---|
wind |
insect |
woman |
person |
song |

1. Click RTK -> Kanji
2. Locate the CSV file containing the RTK definitions and click open
3. Enter a file name and save in your desired folder

---

### The Output
Both functions will result in a similar output - a CSV file containing Kanji and RTK definitions

NB. the title columns are not included

Kanji | RTK
--- | ---
風 | wind
歌 | song
女 | woman
人 | person
来 | coming
週 | week
