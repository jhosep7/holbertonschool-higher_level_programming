#!/usr/bin/python3
"""prints text with 2 newlines after
character - . ? :
"""
def text_indentation(text):
    if isinstance(text, str) == False or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    Temp = text
    if Temp is not None:
            Temp = text.replace(". ", ".\n\n")
            Temp = text.replace("? ", "?\n\n")
            Temp = text.replace(": ", ":\n\n")
    print(Temp, end='')

"""    SpecialChar = ".?:"
    MyStr =  "".join([i if i not in SpecialChar else i + "\n\n" for i in text])

    Output = [j.strip() for j in MyStr.split("\n")]
    print("\n".join(Output), end='')
"""
