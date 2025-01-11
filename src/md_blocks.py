from enum import Enum
import re

def split_blocks(mdtext):
    return mdtext.strip().replace("\n\n\n" , "\n\n").split("\n\n")


class BlockType(Enum):
    HEADER ="Header"
    CODE = "Code"
    QUOTE = "Quote"
    ULIST = "Unordered List"
    OLIST = "Ordered List"
    PAR = "Paragraph"

def label_block(md_block):
    header_regex = r"^(#{1,6} )"
    code_regex = r"^(```)[\s\S]*?(```)$"
    quote_regex = r"^(> )"
    ulist_regex = r"^([-\*] )"
    print(md_block)
    if re.match(header_regex , md_block) != None:
        return BlockType.HEADER
    elif re.match(code_regex , md_block) != None:
        return BlockType.CODE
    elif re.match(quote_regex , md_block) != None:
        return BlockType.QUOTE
    elif re.match(ulist_regex , md_block) != None:
        return BlockType.ULIST
    

    matcho = True
    for i , line in enumerate(md_block.split("\n")):
        if re.match(r"^(" + f"{i + 1}" + r". )" , line) == None:
            matcho = False
    
    
    if matcho:
        return BlockType.OLIST
    
    return BlockType.PAR