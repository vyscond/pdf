class Base (object):
    def __init__ (self,index):
        self.index = index

    def get_reference(self):
        return '{index} 0 R'.format(index=index)

    def reference_array(self,objs):
        return '['+(' '.join([ obj.get_reference() for obj in objs ]))+']'

class Catalog (Base) :
    def __init__ (self,index,page_tree):
        super(Catalog,self).__init__(index)
        self.page_tree = page_tree # pages (int) : id of the page tree

    def __str__ (self):
        return "{index} 0 obj<</Type/Catalog/Pages {pages} R >> endobj % Document Catalog".format(
            index=self.index,
            pages=self.page_tree.get_reference()
        )

# Pages obj
class PageTree (Base) :
    def __init__ (self,index,pages):
        '''pages (list) : list of pages/kids (adobe.objects.Page)'''
        super(PageTree,self).__init__(index)
        #self.kids = '['+(' '.join([ page.get_reference() for page in pages ]))+']' # [ 4 0 R 10 0 R 24 0 R ]
        self.kids = self.reference_array(pages) # [ 4 0 R 10 0 R 24 0 R ]
        self.count = len(self.pages)

    def __str__ (self,index,kids):
        return "{index} 0 obj << /Type /Pages /Kids {kids} /Count {count} >> endobj % Page tree".format(
            index=self.index,
            kids=self.kids,
            count=self.count
        )

class Page (Base) :
    def  __init__(self,parent,contents=None,mediabox=[0,0,612,792]):
        super(Page,self).__init__(index)
        self.mediabox = '['+(' '.join(list(map(str,mediabox))))+']' # [0 0 612 792]
        if contents :
            self.contents = self.reference_array(contents)

    def __str__ (self,index,parent,contents):

        if self.contents :
            self.contents = "/Contents {contents}".format(contents=self.contents)
        else :
            self.contents = ""

        return "{index} 0 obj << /Type /Page /Parent {parent} /MediaBox {mediabox} {contents} >> endobj % {index}s t page".format(
            index=self.index,
            parent=self.parent.get_reference(),
            contents=self.contents,
            mediabox=self.mediabox
        )

class Font (Base) :
    def __init__ (self,index,subtype,basefont):
        super(Font,self).__init__(index)
        self.basefont = basefont
        self.subtype  = subtype

    def __str__ (self):
        return "{index} 0 obj << /Type /Font /Subtype /{subtype} /BaseFont /{basefont} >> endobj % Font".format(
            index=self.index,
            subtype=self.subtype,
            basefont=self.basefont
        )

class Stream (Base):
    def __init__ (self,index,stream):
        super(Stream,self).__init__(index)
        self.stream = stream

    def __str__ (self):
        return "{index} 0 obj << /Length {length} >> stream {stream} endstream endobj % Page contents".format(
            index=self.index,
            length=len(bytes(self.stream,'utf-8')),
            stream=self.stream
        )

class Text (Base):

    def __init__ (self,index,font,coord,text):
        super(Text,self).__init__(index)
        self.font  = font
        self.coord = coord
        self.text  = text

    def __str__ (self):
        # font  - /F13 12 Tf
        # coord - 288 720 Td
        # text  - (ABC) Tj
        return "BT {font} {coord} {text} ET".format(
            index=self.index,
            coord=self.coord,
            text=self.text

        )
