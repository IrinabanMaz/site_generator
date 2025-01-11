from enum import Enum
from HTMLNode import HTMLNode, LeafNode
import re

class TextType(Enum):
    NORMAL="Normal"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:

    def __init__(self , text , text_type , url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self , text_node):
        return (self.text == text_node.text) and (self.text_type == text_node.text_type) and (self.url == text_node.url)
    
    def __repr__(self):
        return f"TextNode({self.text} , {self.text_type.value} , {self.url})"
    

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None , text_node.text)
        case TextType.BOLD:
            return LeafNode("b" , text_node.text)
        case TextType.ITALIC:
            return LeafNode("i" , text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a" , text_node.text , {"href" : text_node.url})
        case TextType.IMAGE:
            return LeafNode("img"  ,text_node.text , {"src" : text_node.url , "alt" : text_node.text})


def split_nodes_delimiter(text_nodes , delimiter , text_type):
    split_nodes = []
    for node in text_nodes:
        if node.text_type == TextType.NORMAL:
            split = node.text.split(delimiter)
            if len(split) % 2 == 0:
                raise SyntaxError("Unclosed markup")
            for i , text in enumerate(split):
                if i%2 == 0:
                    split_nodes.append(TextNode(text , TextType.NORMAL))
                else:
                    split_nodes.append(TextNode(text , text_type))
        else:
            split_nodes.append(node)
        
    return split_nodes

def extract_markdown_images(text):
    image_re = r"!\[.*\]\(.*\)(?!\[)"

    matches = re.findall(image_re , text)

    node_data = []

    for match in matches:
        idx = match.find("]")
        alt = match[2:idx]
        url = match[idx+2:-1]
        node_data.append((alt , url))
    
    return node_data

def extract_markdown_links(text):
    link_re = r"[^!]*\[.*\]\(.*\)(?!\)\[)"

    matches = re.findall(link_re , text)

    node_data = []

    for match in matches:
        idxmin = match.find("[")
        idx = match.find("]")
        alt = match[idxmin+ 1 :idx]
        url = match[idx+2:-1]
        node_data.append((alt , url))
    
    return node_data


def split_node_image(text_nodes):

    split_nodes = []
    for node in text_nodes:
        if node.text_type ==TextType.NORMAL:
            images = extract_markdown_images(node.text)
            last_idx = 0
            for i , image in enumerate(images):
                current_match = f"![{image[0]}]({image[1]})"
                min_idx = node.text.find(current_match)
                split_nodes.append(TextNode(node.text[last_idx:min_idx] , TextType.NORMAL))
                split_nodes.append(TextNode(image[0] , TextType.IMAGE , image[1]))
                last_idx = min_idx + len(current_match)
            
            split_nodes.append(TextNode(node.text[last_idx:] , TextType.NORMAL))
        else:
            split_nodes.append(node)
        
    return split_nodes 


def split_node_link(text_nodes):

    split_nodes = []
    for node in text_nodes:
        if node.text_type ==TextType.NORMAL:
            links = extract_markdown_links(node.text)
            last_idx = 0
            for i , link in enumerate(links):
                current_match = f"[{link[0]}]({link[1]})"
                min_idx = node.text.find(current_match)
                
                split_nodes.append(TextNode(node.text[last_idx:min_idx] , TextType.NORMAL))
                split_nodes.append(TextNode(link[0] , TextType.LINK , link[1]))
                last_idx = min_idx + len(current_match)
            
            split_nodes.append(TextNode(node.text[last_idx:] , TextType.NORMAL))
        else:
            split_nodes.append(node)
        
    return split_nodes 

def text_to_textnodes(text):
    start_node = TextNode(text , TextType.NORMAL)

    image_nodes = split_node_image([start_node])
    link_nodes = split_node_link(image_nodes)
    bold_nodes = split_nodes_delimiter(link_nodes , "**" , TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes , "*" , TextType.ITALIC)
    final_nodes = split_nodes_delimiter(italic_nodes , "`" , TextType.CODE)

    return final_nodes