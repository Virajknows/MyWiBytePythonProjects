import sys
import time


def slow_print(text="", delay=0.03, end="\n"):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()


def encode_even_odd(text):
    result = ""
    i = 0
    while i < len(text) - 1:
        result += text[i + 1] + text[i]
        i += 2
    if i < len(text):
        result += text[i]
    return result


def decode_even_odd(text):
    return encode_even_odd(text)


def encode_reverse(text):
    return text[::-1]


def decode_reverse(text):
    return text[::-1]


def encode_words(text):
    words = text.split(" ")
    words.reverse()
    return " ".join(words)


def decode_words(text):
    words = text.split(" ")
    words.reverse()
    return " ".join(words)


def encode_halves(text):
    middle = len(text) // 2
    return text[middle:] + text[:middle]


def decode_halves(text):
    middle = len(text) // 2
    split_point = len(text) - middle
    return text[split_point:] + text[:split_point]


def encode_caesar(text, shift):
    result = ""
    for letter in text:
        if letter.isalpha():
            start = ord("A") if letter.isupper() else ord("a")
            result += chr((ord(letter) - start + shift) % 26 + start)
        else:
            result += letter
    return result


def decode_caesar(text, shift):
    return encode_caesar(text, -shift)


slow_print("Enter your secret message: ", end="")
message = input()
slow_print()
slow_print("Original message: " + message)
slow_print()

encoded = encode_even_odd(message)
decoded = decode_even_odd(encoded)
slow_print("Swap even and odd letters")
slow_print("Encoded: " + encoded)
slow_print("Decoded: " + decoded)
slow_print()

encoded = encode_reverse(message)
decoded = decode_reverse(encoded)
slow_print("Reverse the string")
slow_print("Encoded: " + encoded)
slow_print("Decoded: " + decoded)
slow_print()

encoded = encode_words(message)
decoded = decode_words(encoded)
slow_print("Reverse the string word by word")
slow_print("Encoded: " + encoded)
slow_print("Decoded: " + decoded)
slow_print()

encoded = encode_halves(message)
decoded = decode_halves(encoded)
slow_print("Swap the first and second halves")
slow_print("Encoded: " + encoded)
slow_print("Decoded: " + decoded)
slow_print()

encoded = encode_caesar(message, 3)
decoded = decode_caesar(encoded, 3)
slow_print("Bonus: Caesar cipher with a shift of 3")
slow_print("Encoded: " + encoded)
slow_print("Decoded: " + decoded)
slow_print()

encoded = encode_caesar(encode_halves(encode_reverse(message)), 5)
decoded = decode_reverse(decode_halves(decode_caesar(encoded, 5)))
slow_print("Bonus: Reverse, then swap halves, then Caesar cipher with a shift of 5")
slow_print("Encoded: " + encoded)
slow_print("Decoded: " + decoded)
slow_print()

if decoded == message:
    slow_print("Every encoding was decoded back to the original message.")
