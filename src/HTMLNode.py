

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