# The Food Files!

Eating a balanced diet is hard, but **JSON makes finding nutritious foods easy!** This repository explores the conversion of raw files into JSON format (`main.py`). The `data` directory contains all raw data relating to food, including name, GI, fiber content, and fat content. These files are imported and cleaned, including steps for **deduping**, **removing blanks**, and **removing unusable answers**. These data are then compiled into dictionaries and are saved to the JSON file `food.json`. This JSON file is then read into `stats.py` to give statistics related to **iconic foods**, those foods that achieve **low GI**, **low fat**, and **high fiber**!

*Creator: Jack Lynn (Dev10 Data Associate)*

## How to Run

**Prerequisite:** Requires Python 3.8 or later.

**Step 1:** Download the Git repository from [here](https://github.com/jackrlynn3/word-guessing-game).

**Step 2:** Open your Terminal window or your operating system's equivalent command line.

**Step 3:** Run the following Python command to get JSON file:

    python main.py

**Step 4:** Run the following Python command to get stats:

    python stats.py
