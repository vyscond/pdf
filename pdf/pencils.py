import pdf

class Pencil (object) :
    def __init__ (self,content=''):
        self.content = content

class TextBox (Pencil) :
    def __init__ (self,content='',font=pdf.fonts.TimesRoman(),x=0,y=0,width=0,height=0):
        super(Text,self).__init__(content)

    def __str__ (self):
        return pdf.adobe.objects.
