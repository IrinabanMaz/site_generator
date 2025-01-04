import unittest

from textnode import TextNode , TextType

class TestTextNode(unittest.TestCase)
    def test_eq(self):
        node  = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node , node2)

    def test_eq2(self):
        node  = TextNode("test node for test 2", TextType.IMAGE , "www.google.com")
        node2 = TextNode("test node for test 2", TextType.IMAGE, "www.google.com")
        self.assertEqual(node , node2)

    def test_neq(self):
        node  = TextNode("test node for test 3", TextType.IMAGE , "www.google.com")
        node2 = TextNode("test node for test 3", TextType.LINK, "www.google.com")
        self.assertNotEqual(node , node2)
    


if __name__ == "__main__":
    unittest.main()