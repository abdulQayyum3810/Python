from translate import Translator
translator=Translator(to_lang="ja")
try:
    with open("translate_text.txt",mode="r") as my_file:
        text=my_file.read()
        translation=translator.translate(text)
        print(translation)
        """with open("./translated_text.txt",mode="w") as my_file2:
            my_file2.write(translation)  # Windows cant write this use linux"""
except FileNotFoundError:
    print("file is not found")