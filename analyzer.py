"""
Smart Text Analyzer
A CLI tool to analyze text metrics including word count, character count,
sentence count, word frequency distribution, average word length,
longest word, and estimated reading time.

Usage:
    python analyzer.py              # paste text interactively
    python analyzer.py -f notes.txt # analyze a text file
"""

import argparse
import re
from collections import Counter

WORDS_PER_MINUTE = 200  # average adult reading speed


def analyze_text(text: str) -> dict:
    """Compute all metrics for the given text and return them as a dict."""
    if not text.strip():
        return {}

    words = re.findall(r"\b\w+\b", text.lower())
    total_words = len(words)
    total_chars = len(text)
    total_chars_no_spaces = len(text.replace(" ", "").replace("\n", ""))

    sentence_parts = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    total_sentences = max(len(sentence_parts), 1)

    avg_word_length = round(sum(len(w) for w in words) / total_words, 2) if words else 0
    longest_word = max(words, key=len) if words else ""
    reading_time_min = max(round(total_words / WORDS_PER_MINUTE, 2), 0.01)

    word_freq = Counter(words).most_common(5)

    return {
        "total_chars": total_chars,
        "total_chars_no_spaces": total_chars_no_spaces,
        "total_words": total_words,
        "total_sentences": total_sentences,
        "avg_word_length": avg_word_length,
        "longest_word": longest_word,
        "reading_time_min": reading_time_min,
        "word_freq": word_freq,
    }


def print_report(stats: dict) -> None:
    if not stats:
        print("Provided text is empty.")
        return

    print("\n--- TEXT ANALYSIS RESULTS ---")
    print(f"Total Characters       : {stats['total_chars']}")
    print(f"Characters (no spaces) : {stats['total_chars_no_spaces']}")
    print(f"Total Words            : {stats['total_words']}")
    print(f"Total Sentences        : {stats['total_sentences']}")
    print(f"Average Word Length    : {stats['avg_word_length']}")
    print(f"Longest Word           : {stats['longest_word']}")
    print(f"Estimated Reading Time : {stats['reading_time_min']} min")

    print("\nMost Common Words:")
    if stats["word_freq"]:
        for word, count in stats["word_freq"]:
            print(f" - {word}: {count}")
    else:
        print(" (no words found)")
    print("-----------------------------\n")


def get_text_from_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    parser = argparse.ArgumentParser(description="Smart Text Analyzer - analyze text metrics")
    parser.add_argument(
        "-f", "--file",
        help="Path to a .txt file to analyze (skips interactive input)"
    )
    args = parser.parse_args()

    print("=== Smart Text Analyzer ===")

    if args.file:
        try:
            text = get_text_from_file(args.file)
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return
        except UnicodeDecodeError:
            print(f"Error: Could not read '{args.file}' — is it a valid text file?")
            return
    else:
        text = input("Enter or paste your text here:\n")

    stats = analyze_text(text)
    print_report(stats)


if __name__ == "__main__":
    main()  

