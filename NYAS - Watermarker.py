def embed_watermark(text):
    watermark_pattern = ['\u200B', '\u200C', '\u200D', '\uFEFF']  # Zero-width spaces
    words = text.split()
    watermarked_text = ""
    for i, word in enumerate(words):
        space = watermark_pattern[i % len(watermark_pattern)]
        watermarked_text += word + space + ' '
    return watermarked_text

original_text = input("Enter your text: ")

watermarked_text = embed_watermark(original_text)

print("Original text:", original_text)
print("Watermarked text:", watermarked_text)
