from oled import show_text

def out(text, height=8):
    print(text)
    y = 0
    if '\n' in text:
        txts = text.split('\n')
    else:
        n = 16
        txts = [text[i:i+n] for i in range(0, len(text), n)]
    for txt in txts:
        show_text(txt, start_h=y * height, clean=y==0)
        y += 1
