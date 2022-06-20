#import the module
from translate import Translator
#you can specify any international language
translator = Translator(to_lang = "spanish")
#typing the message
translation = translator.translate("welcome to Tamilnadu")
#print the translated message
print(translation)