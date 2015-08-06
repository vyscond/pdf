# All modules were developed based on http://www.adobe.com/content/dam/Adobe/en/devnet/acrobat/pdfs/PDF32000_2008.pdf

# Size (integer) : (Required; shall not be an indirect reference) The total number of entries in
#                  the file’s cross-reference table, as defined by the combination of the original
#                  section and all update sections. Equivalently, this value shall be 1 greater
#                  than the highest object number defined in the file.
#                  Any object in a cross-reference section whose number is greater than this
#                  value shall be ignored and defined to be missing by a conforming reader.

VERSIONS = {
    10 : "%PDF–1.0",
    11 : "%PDF–1.1",
    12 : "%PDF–1.2",
    13 : "%PDF–1.3",
    14 : "%PDF–1.4",
    15 : "%PDF–1.5",
    16 : "%PDF–1.6",
    17 : "%PDF–1.7",
}

BaseTemplate = '''
{version}
{body}
trailer
<</Size {size}
/Root 1 0 R>>
startxref
{startxref}
%%EOF'''.strip()
