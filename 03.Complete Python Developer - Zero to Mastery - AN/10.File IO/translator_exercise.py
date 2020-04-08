#https://pypi.org/project/translate/
from translate import Translator

translator= Translator(to_lang="ja")

try:
    with open('source.txt','r') as my_file:
        with open('translated_one.txt','w',encoding="utf-8") as my_file2:
            for text in my_file.readlines():
                translation = translator.translate(text)
                print(translation)
                my_file2.write(translation+"\n")
            
except Exception as e:
    print(f"opps! error occured {e}")

