from string_package import (
    reverse_string,
    capitalize_words,
    remove_punctuation,
    count_characters,
    count_words,
    average_word_length
)


def main():
    # Read input from user
    sentence = input("Enter a sentence to analyze: ")

    # Process and display results
    print("\nAnalysis Results:")
    print(f"Reversed: {reverse_string(sentence)}")
    print(f"Capitalized: {capitalize_words(sentence)}")

    no_punct = remove_punctuation(sentence)
    print(f"\nWithout punctuation: {no_punct}")
    print(f"Character count: {count_characters(no_punct)}")
    print(f"Word count: {count_words(no_punct)}")
    print(f"Average word length: {average_word_length(no_punct):.2f}")


if __name__ == "__main__":
    main()