# Smart Text Analyzer

A simple Python CLI tool that analyzes text and gives you useful metrics like word count, character count, sentence count, word frequency, and estimated reading time.

## Features

- Total character and word count
- Sentence count
- Average word length
- Longest word in the text
- Top 5 most frequently used words
- Estimated reading time
- Analyze text directly from the terminal or from a `.txt` file

## How to Run

Make sure you have Python installed, then run:

```bash
python analyzer.py

To analyze text from a file instead:

python analyzer.py -f notes.txt

## Example

=== Smart Text Analyzer ===
Enter or paste your text here:
This is a test. This is only a test!

--- TEXT ANALYSIS RESULTS ---
Total Characters       : 36
Characters (no spaces) : 30
Total Words            : 8
Total Sentences        : 2
Average Word Length    : 3.5
Longest Word           : test
Estimated Reading Time : 0.04 min

Most Common Words:
 - this: 2
 - is: 2
 - a: 1
 - test: 2
 - only: 1
-----------------------------

## Author

Built by Pragnya Paramita Mekap
