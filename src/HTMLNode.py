

class HTMLNode:
    def __init__(self ,tag = None , value = None , children = None , props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        
        return " " + " ".join(
            list(
                map(
                    lambda i: f"{i[0]}=\"{i[1]}\"" , self.props.items())))

    def __repr__(self):
        return f"HTMLNode({self.tag} ,{self.value } , {self.children} , {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self ,tag , value , props = None):
        super().__init__(tag , value , None , props)
        
    def to_html(self):
            if self.value == None:
                raise ValueError
            if self.tag == None:
                return self.value
            
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self,tag , children , props = None):
        super().__init__(tag , None, children , props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("missing tag")
        if self.children == []:
            raise ValueError("missing children")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        if self.props ==None:
            return f"<{self.tag}>" + children_html + f"</{self.tag}>"
        
        return f"<{self.tag}{self.props_to_html()}>" + children_html + f"</{self.tag}>"