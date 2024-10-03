def analyze_watermark(text):
    # Zero-width characters
    zero_width_chars = {
        'Zero Width Space (U+200B)': '\u200B',
        'Zero Width Non-Joiner (U+200C)': '\u200C',
        'Zero Width Joiner (U+200D)': '\u200D',
        'Zero Width No-Break Space (U+FEFF)': '\uFEFF'
    }

    total_length = len(text)
    found = False

    for name, char in zero_width_chars.items():
        count = text.count(char)
        if count > 0:
            found = True
            frequency = (count / total_length) * 100 if total_length > 0 else 0
            print(f'{name} found {count} times. Frequency: {frequency:.2f}%')

    if not found:
        print('No zero-width characters found.')


watermarked_text = input("Put the text that you want to test: ")
analyze_watermark(watermarked_text)
