import HTMLNode
import textnode
import md_blocks
import re


def markdown_to_html(md_text):

    html = []
    blocks = md_blocks.split_blocks(md_text)

    for block in blocks:
        btype = md_blocks.label_block(block)

        match btype:
            case md_blocks.BlockType.HEADER:
                idx = block.find(" ")
                header_tag = f"h{idx}"
                content = block[idx+1:]
                nodes = textnode.text_to_textnodes(content)
                leaf_nodes = list(map(textnode.text_node_to_html_node , nodes))
                header_node = HTMLNode.ParentNode(header_tag , leaf_nodes)
                html.append(header_node)
            case md_blocks.BlockType.CODE:
                code_tag = "code"
                content = block[3:-3]
                nodes = textnode.text_to_textnodes(content)
                leaf_nodes = list(map(textnode.text_node_to_html_node , nodes))
                code_node = HTMLNode.ParentNode(code_tag , leaf_nodes)
                html.append(code_node)
            case md_blocks.BlockType.QUOTE:
                quote_tag = "blockquote"
                content = block.replace("> " , "")
                nodes = textnode.text_to_textnodes(content)
                leaf_nodes = list(map(textnode.text_node_to_html_node , nodes))
                quote_node = HTMLNode.ParentNode(quote_tag , leaf_nodes)
                html.append(quote_node)
            case md_blocks.BlockType.ULIST:
                list_tag = "ul"
                line_nodes = []
                for line in block.split("\n"):
                    content = line[2:]
                    item_tag = "li"
                    nodes = textnode.text_to_textnodes(content)
                    leaf_nodes = list(map(textnode.text_node_to_html_node , nodes))
                    item_node = HTMLNode.ParentNode(item_tag , leaf_nodes)
                    line_nodes.append(item_node)
                
                list_node = HTMLNode.ParentNode(list_tag , line_nodes)
                html.append(list_node)
            
            case md_blocks.BlockType.OLIST:
                list_tag = "ol"
                line_nodes = []
                for line in block.split("\n"):
                    content = line[3:]
                    item_tag = "li"
                    nodes = textnode.text_to_textnodes(content)
                    leaf_nodes = list(map(textnode.text_node_to_html_node , nodes))
                    item_node = HTMLNode.ParentNode(item_tag , leaf_nodes)
                    line_nodes.append(item_node)
                
                list_node = HTMLNode.ParentNode(list_tag , line_nodes)
                html.append(list_node)

            case md_blocks.BlockType.PAR:
                par_tag = "p"
                content = block        
                nodes = textnode.text_to_textnodes(content)
                leaf_nodes = list(map(textnode.text_node_to_html_node , nodes))
                par_node = HTMLNode.ParentNode(par_tag , leaf_nodes)
                html.append(par_node)
        
    
    return HTMLNode.ParentNode("div" , html)

def extract_title(md_text):
    blocks = md_blocks.split_blocks(md_text)

    for block in blocks:
        title_re = r"^(# )"
        if re.match(title_re , block) != None:
            return block[2:].strip()
        
    raise Exception("No title found(no h1 header).")