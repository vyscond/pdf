import codecs
import pdf


def metric (value,unit=None):
    units = {
        "cm"   : 72 / 2.54,
        "mm"   : 72 / 25.4,
        "inch" : 72.
    }

    if unit :
        return value * units[unit]
    else: # set value as computer points
        return value

class Layout (object) :

    # metrics on mm
    builtins = {
        "a4" : [ metric(210,'mm'), metric(297,'mm'), metric(1,'mm')],
        "a5" : [ metric(148,'mm'), metric(210,'mm'), metric(1,'mm')],
    }

    def __init__ (self,builtin=None):
        frmt = Layout.builtins['a4']
        if builtin :
            frmt  = Layout.builtins[builtin]
        self.width , self.height  , self.margin  = Layout.builtins[builtin]

    def mediabox(self):
        return [0,0,self.width,self.height]

class Base (object):
    def __init__ (self,index):
        self.index = index

    def get_reference(self):
        return '{index} 0 R'.format(index=index)

    def reference_array(self,objs):
        return '['+(' '.join([ obj.get_reference() for obj in objs ]))+']'

# /Page
class Page (Base) :
    def  __init__(self,parent,contents=None,mediabox=[0,0,612,792]):
        super(Page,self).__init__(index)
        self.mediabox = '['+(' '.join(list(map(str,mediabox))))+']' # [0 0 612 792]
        if contents :
            self.contents = self.reference_array(contents)

    def __str__ (self):

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

# /Pages obj
class Pages (Base) :

    def __init__ (self,index,layout):
        super(PageTree,self).__init__(index)

        self.kids  = []

        self.layout = layout

        self.fonts = []

    def add_page(self,):
        self.kids.append(
            Page( self.index + (len(self.kids)+1) , self.layout.mediabox() )
        )

    def write(self,pencil):

        # TODO the magic is here

        # 1 - Check the font is already used

    def __str__ (self,index,kids):
        ret = "{index} 0 obj << /Type /Pages /Kids {kids} /Count {count} >> endobj % Page tree\n".format(
            index=self.index,
            kids=self.reference_array(self.kids), # [ 4 0 R 10 0 R 24 0 R ]
            count=len(self.kids)
        )
        ret += str(self.kids)
        return ret

# /Catalog
class Catalog (object):

    def __init__ (self,index,layout):
        super(Catalog,self).__init__(index)
        self.pages = Pages(self.index+1,layout)
        self.pages.add_page()

    def __str__ (self):
        ret = "{index} 0 obj<</Type/Catalog/Pages {pages} R >> endobj % Document Catalog\n".format(
            index=self.index,
            pages=self.pages.get_reference()
        )

        ret += str(self.pages)

        return ret

class Document (object) :

    def __init__ (self,layout=Layout('a4'),version=16):

        self.version = {
            10 : "%PDF–1.0",
            11 : "%PDF–1.1",
            12 : "%PDF–1.2",
            13 : "%PDF–1.3",
            14 : "%PDF–1.4",
            15 : "%PDF–1.5",
            16 : "%PDF–1.6",
            17 : "%PDF–1.7",
        }[version]

        self.layout = layout

        self.catalog = Catalog(1,self.layout)

    def write(self,pencil):

        self.catalog.write(pencil)

    def __str__ (self):

        return (
            self.version + '\n'
            str(self.catalog) + '\n'
        )
