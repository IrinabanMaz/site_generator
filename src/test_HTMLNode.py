import unittest
from HTMLNode import HTMLNode , LeafNode , ParentNode

class test_HTMLNode(unittest.TestCase):
    def test_propsHTML1(self):
        props = {
    "href": "https://www.google.com", 
    "target": "_blank",
    }   
        node = HTMLNode(None , None , None ,  props)
        self.assertEqual(node.props_to_html() ,  " href=\"https://www.google.com\" target=\"_blank\"")


    def test_propsHTML2(self):
        props = {
            "href" : "https://yahoo.com"
        }
        node = HTMLNode(None , None , None , props)
        self.assertEqual(node.props_to_html() , " href=\"https://yahoo.com\"")
    
    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError , node.to_html)


class test_LeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html() , "<p>This is a paragraph of text.</p>")

    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html() , "<a href=\"https://www.google.com\">Click me!</a>")

    def test_to_html3(self):
        node = LeafNode(None, "some sample text")
        self.assertEqual(node.to_html() , "some sample text")
    
    def test_to_html4(self):
        node = LeafNode(None, None)
        self.assertRaises(ValueError , node.to_html)

class test_ParentNode(unittest.TestCase):
    def test_testParent1(self):
        target = (open("src/test_files/html_test1.html" , "r").
                  read().
                  replace("\n" , "").
                  replace("  ", ""))
        leaf1 = LeafNode("title" , "Sample 1")
        parent1 = ParentNode("head" , [leaf1])

        leaf21 = LeafNode("h1" , "Welcome to Sample 1")
        leaf221 = LeafNode(None , "This is a paragraph with ")
        leaf222 = LeafNode("span" , "bold text")
        leaf223 = LeafNode(None, ".")
        parent22 = ParentNode("p" , [leaf221 , leaf222 , leaf223])

        parent2 = ParentNode("body" , [leaf21 , parent22])

        parent = ParentNode("html" , [parent1 , parent2])



        self.assertEqual(parent.to_html() , target)
        

