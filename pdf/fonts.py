# Read pg. 254

class Font (object) :
    def __init__ (self,basefont,subtype,size):
        self.basefont = basefont
        self.subtype  = subtype
        self.size = size
        self.index = 0

    def __eq__(self, font):
        if isinstance(font, Font):
            return ( self.basefont == font.basefont and
                self.subtype == font.subtype and
                self.size == font.size )
        return NotImplemented

        return

    def __str__ (self):
        return "{index} 0 obj << /Type /Font /Subtype /{subtype} /BaseFont /{basefont} >> endobj % Font".format(
            index=self.index,
            subtype=self.subtype,
            basefont=self.basefont
        )

class TimesRoman (Font):
    def __init__(self,size):
        super().__init__('Times-Roman','Type1',size)

class TimesBold (Font):
    def __init__(self,size):
        super().__init__('Times-Bold','Type1',size)

class TimesItalic  (Font):
    def __init__(self,size):
        super().__init__('Times-Italic','Type1',size)

class TimesBoldItalic (Font):
    def __init__(self,size):
        super().__init__('Times-BoldItalic','Type1',size)

class Helvetica (Font):
    def __init__(self,size):
        super().__init__('Helvetica','Type1',size)

class HelveticaBold (Font):
    def __init__(self,size):
        super().__init__('Helvetica-Bold','Type1',size)

class HelveticaOblique (Font):
    def __init__(self,size):
        super().__init__('HelveticaOblique','Type1',size)

class HelveticaBoldOblique (Font):
    def __init__(self,size):
        super().__init__('Helvetica-BoldOblique','Type1',size)

class Courier (Font):
    def __init__(self,size):
        super().__init__('Courier','Type1',size)

class CourierBold (Font):
    def __init__(self,size):
        super().__init__('Courier-Bold','Type1',size)

class CourierOblique  (Font):
    def __init__(self,size):
        super().__init__('Courier-Oblique','Type1',size)

class CourierBoldOblique (Font):
    def __init__(self,size):
        super().__init__('Courier-BoldOblique','Type1',size)

class Symbol (Font):
    def __init__(self,size):
        super().__init__('Symbol','Type1',size)

class ZapfDingbats  (Font):
    def __init__(self,size):
        super().__init__('ZapfDingbats','Type1',size)
