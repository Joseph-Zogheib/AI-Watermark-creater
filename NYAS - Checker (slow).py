watermarked_text = input("put the text that you want to test")

chars = set('\u200B')
if any((c in chars) for c in watermarked_text):
    print('Found')
else:
    chars = set('\u200C')
    if any((c in chars) for c in watermarked_text):
        print('Found')
    else:
        chars = set('\u200D')
        if any((c in chars) for c in watermarked_text):
            print('Found')
        else:
            chars = set('\uFEFF')
            if any((c in chars) for c in watermarked_text):
                print('Found')
            else:
                print('Not Found')
