import unittest

from textnode import TextNode , TextType 
from textnode import (split_nodes_delimiter , 
                      extract_markdown_images, extract_markdown_links,
                         split_node_image , split_node_link,
                         text_to_textnodes)

class TestTextNode(unittest.TestCase):
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
    

class test_split_nodes(unittest.TestCase):
    def test_split_nodes1(self):
        text = open("src/test_files/split_nodes_test1.md" , "r").read()

        start_node = TextNode(text , TextType.NORMAL)
        nodes = split_nodes_delimiter([start_node] , "**" , TextType.BOLD)

        true_nodes = [TextNode("Hello, fellow adventurers! My name is " , TextType.NORMAL)]
        true_nodes.append(TextNode("Ward Rackley" , TextType.BOLD))
        true_nodes.append(TextNode(", an Undead Male Warlock who roams the lands of Azeroth in search of power, secrets, and forbidden knowledge. Below is a glimpse into my journey." , TextType.NORMAL))
        self.assertEqual(nodes , true_nodes)
    
    def test_split_nodes2(self):

        text = open("src/test_files/split_nodes_test2.md" , "r").read()
        
        start_node = TextNode(text , TextType.NORMAL)
        int_nodes = split_nodes_delimiter([start_node] , "**" , TextType.BOLD)
        final_nodes = split_nodes_delimiter(int_nodes , "*" , TextType.ITALIC)

        true_nodes = [TextNode("Reach Level " , TextType.NORMAL)]
        true_nodes.append(TextNode("60" , TextType.BOLD))
        true_nodes.append(TextNode(" and obtain the " , TextType.NORMAL))
        true_nodes.append(TextNode("Dreadsteed" , TextType.ITALIC))
        true_nodes.append(TextNode("." , TextType.NORMAL))

        self.assertEqual(final_nodes , true_nodes)

    def test_split_nodes3(self):
        text = open("src/test_files/split_nodes_test3.md" , "r").read()

        start_node = TextNode(text , TextType.NORMAL)
        nodes = split_nodes_delimiter([start_node] , "**" , TextType.BOLD)

        true_nodes = [TextNode("- " , TextType.NORMAL)]
        true_nodes.append(TextNode("Shadow Bolt" , TextType.BOLD))
        true_nodes.append(TextNode(": Hurl bolts of shadow energy to devastate enemies.  \n- " , TextType.NORMAL))
        true_nodes.append(TextNode("Summon Minions" , TextType.BOLD))
        true_nodes.append(TextNode(": Call forth infernals, voidwalkers, or imps to aid in battle.  \n- " , TextType.NORMAL))
        true_nodes.append(TextNode("Curse of Agony" , TextType.BOLD))
        true_nodes.append(TextNode(": Slowly drains the life of my enemies.  \n- " , TextType.NORMAL))
        true_nodes.append(TextNode("Soulstone Resurrection" , TextType.BOLD))
        true_nodes.append(TextNode(": Prepare for the inevitable wipe." , TextType.NORMAL))

        self.assertEqual(nodes , true_nodes)


class test_extract_link(unittest.TestCase):
    def test_extract_images(self):
        text = open("src/test_files/extract_links_test1.md" , "r").read()

        images = extract_markdown_images(text)

        true_images = [("Ward Rackley in Action","https://via.placeholder.com/800x400.png")]
        true_images.append(("Voidwalker Companion","https://via.placeholder.com/400x200.png") )
        true_images.append(("Felhunter Companion","https://via.placeholder.com/400x200.png"))

        self.assertEqual(images, true_images)

    def test_extract_links(self):
        text = open("src/test_files/extract_links_test1.md" , "r").read()

        links = extract_markdown_links(text)

        true_links = [("Tirisfal Glades","https://wowpedia.fandom.com/wiki/Tirisfal_Glades")]
        true_links.append(("Scarlet Monastery" ,"https://wowpedia.fandom.com/wiki/Scarlet_Monastery"))
        true_links.append(("Burning Steppes" , "https://wowpedia.fandom.com/wiki/Burning_Steppes"))
        true_links.append(("Check out this guide to Warlock PvP", "https://www.icy-veins.com/wow/warlock-pvp-guide"))
        true_links.append(("View the best gear setups","https://www.wowhead.com"))
   
        self.assertEqual(links, true_links)


class test_split_image_file(unittest.TestCase):
    def test_split_image(self):
        text = (open("src/test_files/extract_links_test1.md" , "r").
                read()
        )
        nodes = split_node_image([TextNode(text, TextType.NORMAL)])

        true_nodes = [TextNode("\n\nWelcome to the chronicles of **Ward Rackley**, the infamous undead warlock. Explore my journey through Azeroth and beyond.\n\n" , TextType.NORMAL)]
        true_nodes.append(TextNode("Ward Rackley in Action" , TextType.IMAGE , "https://via.placeholder.com/800x400.png"))
        true_nodes.append(TextNode("\n\n## Key Locations I've Conquered\n\n- [Tirisfal Glades](https://wowpedia.fandom.com/wiki/Tirisfal_Glades) – My haunting homeland.\n- [Scarlet Monastery](https://wowpedia.fandom.com/wiki/Scarlet_Monastery) – A stronghold I decimated with fire and shadow.\n- [Burning Steppes](https://wowpedia.fandom.com/wiki/Burning_Steppes) – Where molten enemies fell before my might.\n\n## My Trusted Companions\n\n",
                            TextType.NORMAL))
        true_nodes.append(TextNode("Voidwalker Companion",TextType.IMAGE ,"https://via.placeholder.com/400x200.png"))
        true_nodes.append(TextNode("  \nMy Voidwalker, always ready to tank any foe.\n\n" , TextType.NORMAL))
        true_nodes.append(TextNode("Felhunter Companion" , TextType.IMAGE , "https://via.placeholder.com/400x200.png" ))
        true_nodes.append(TextNode("  \nThe Felhunter, ever vigilant for enemy casters.\n\n## Share Your Adventures!\n\nFeel free to share your own tales of conquest by linking to your favorite stories or images! For example:\n\n- [Check out this guide to Warlock PvP](https://www.icy-veins.com/wow/warlock-pvp-guide).\n- [View the best gear setups](https://www.wowhead.com).\n\n---\n\nLet me know if you'd like me to generate links to specific WoW resources or lore pages!",
                                   TextType.NORMAL))
        
        self.assertEqual(nodes , true_nodes)
    
    def test_split_link(self):
        text = (open("src/test_files/extract_links_test1.md" , "r").
                read()
        )
        nodes = split_node_link([TextNode(text, TextType.NORMAL)])

        true_nodes = [TextNode("\n\nWelcome to the chronicles of **Ward Rackley**, the infamous undead warlock. Explore my journey through Azeroth and beyond.\n\n![Ward Rackley in Action](https://via.placeholder.com/800x400.png)\n\n## Key Locations I've Conquered\n\n- ",
                               TextType.NORMAL)]
        
        true_nodes.append(TextNode("Tirisfal Glades" , TextType.LINK,"https://wowpedia.fandom.com/wiki/Tirisfal_Glades"))
        true_nodes.append(TextNode(" – My haunting homeland.\n- " , TextType.NORMAL))
        true_nodes.append(TextNode("Scarlet Monastery" , TextType.LINK , "https://wowpedia.fandom.com/wiki/Scarlet_Monastery"))
        true_nodes.append(TextNode(" – A stronghold I decimated with fire and shadow.\n- " , TextType.NORMAL))
        true_nodes.append(TextNode("Burning Steppes" , TextType.LINK , "https://wowpedia.fandom.com/wiki/Burning_Steppes"))
        true_nodes.append(TextNode(" – Where molten enemies fell before my might.\n\n## My Trusted Companions\n\n![Voidwalker Companion](https://via.placeholder.com/400x200.png)  \nMy Voidwalker, always ready to tank any foe.\n\n![Felhunter Companion](https://via.placeholder.com/400x200.png)  \nThe Felhunter, ever vigilant for enemy casters.\n\n## Share Your Adventures!\n\nFeel free to share your own tales of conquest by linking to your favorite stories or images! For example:\n\n- ",
                                   TextType.NORMAL))
        true_nodes.append(TextNode("Check out this guide to Warlock PvP", TextType.LINK,"https://www.icy-veins.com/wow/warlock-pvp-guide"))
        true_nodes.append(TextNode(".\n- " , TextType.NORMAL))
        true_nodes.append(TextNode("View the best gear setups" , TextType.LINK,"https://www.wowhead.com"))
        true_nodes.append(TextNode(".\n\n---\n\nLet me know if you'd like me to generate links to specific WoW resources or lore pages!",
                                   TextType.NORMAL))
        
        self.assertEqual(nodes , true_nodes)


class test_text_to_textnodes(unittest.TestCase):
    def test_text_totextnodes(self):
        text = open("src/test_files/test_text_to_textnodes.md" , "r").read()

        nodes = text_to_textnodes(text)

        true_nodes = [TextNode("# The Chronicles of Ward Rackley\n\nWelcome to the dark and twisted tales of ",
                               TextType.NORMAL)]
        true_nodes.append(TextNode("Ward Rackley" , TextType.BOLD))
        true_nodes.append(TextNode(", " , TextType.NORMAL))
        true_nodes.append(TextNode("Undead Warlock" , TextType.ITALIC))
        true_nodes.append(TextNode(" of Azeroth.\n\n---\n\n## My Arsenal of Chaos\n\n",
                          TextType.NORMAL))
        true_nodes.append(TextNode("Here are some of my favorite spells and abilities:" ,
                          TextType.ITALIC))
        true_nodes.append(TextNode("\n\n- " , TextType.NORMAL))
        true_nodes.append(TextNode("Shadow Bolt" , TextType.BOLD))
        true_nodes.append(TextNode(": " , TextType.NORMAL))
        true_nodes.append(TextNode("Unleash devastating shadow energy upon my enemies.",
                          TextType.ITALIC))
        true_nodes.append(TextNode("  \n- ",TextType.NORMAL))
        true_nodes.append(TextNode("Summon Demon" , TextType.BOLD))
        true_nodes.append(TextNode(": Call forth a loyal servant to fight by my side.  \n- `Soulstone`: " , 
                          TextType.NORMAL))
        true_nodes.append(TextNode("Cheat death itself." , TextType.ITALIC))
        true_nodes.append(TextNode("  \n\n> " , TextType.NORMAL))
        true_nodes.append(TextNode("\"Power comes at a price, but it's a price I'm willing to pay.\"",
                                    TextType.ITALIC))
        true_nodes.append(TextNode(" – " , TextType.NORMAL))
        true_nodes.append(TextNode("Ward Rackley" , TextType.BOLD))
        true_nodes.append(TextNode("\n\n---\n\n## Places I've Conquered  \n\n- ",
                          TextType.NORMAL))
        true_nodes.append(TextNode("Scarlet Monastery",TextType.LINK,"https://wowpedia.fandom.com/wiki/Scarlet_Monastery"))
        true_nodes.append(TextNode(": A den of zealots who fell to my fire and shadow.  \n- ",
                                   TextType.NORMAL))
        true_nodes.append(TextNode("Burning Steppes",TextType.LINK ,"https://wowpedia.fandom.com/wiki/Burning_Steppes"))
        true_nodes.append(TextNode(": ", TextType.NORMAL))
        true_nodes.append(TextNode("Where the ground burns as fiercely as my soul." , 
                                   TextType.ITALIC))
        true_nodes.append(TextNode("  \n\n" , TextType.NORMAL))
        true_nodes.append(TextNode("Ward Rackley in Action" , TextType.IMAGE,"https://via.placeholder.com/800x400.png"))
        true_nodes.append(TextNode("\n\n---\n\n## Pro Tips for Aspiring Warlocks  \n\nHere’s a bit of code to maximize your DPS rotation:\n\n",
                          TextType.NORMAL))
        true_nodes.append(TextNode("\n/castsequence reset=target Corruption, Curse of Agony, Shadow Bolt\n",
                          TextType.CODE))
        true_nodes.append(TextNode("" , TextType.NORMAL))

        self.assertEqual(nodes, true_nodes)






if __name__ == "__main__":
    unittest.main()