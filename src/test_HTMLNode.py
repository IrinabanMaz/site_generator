import unittest
from HTMLNode import HTMLNode

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
