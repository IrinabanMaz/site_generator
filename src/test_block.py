import unittest
from md_blocks import( split_blocks , 
            BlockType ,label_block)


class test_split_blocks(unittest.TestCase):
    def test_split_blocks(self):
        text = open("src/test_files/test_text_to_textnodes.md" , "r").read()

        blocks = split_blocks(text)

        true_blocks = ["# The Chronicles of Ward Rackley"]
        true_blocks.append("Welcome to the dark and twisted tales of **Ward Rackley**, *Undead Warlock* of Azeroth.")
        true_blocks.append("---")
        true_blocks.append("## My Arsenal of Chaos")
        true_blocks.append("*Here are some of my favorite spells and abilities:*")
        true_blocks.append("- **Shadow Bolt**: *Unleash devastating shadow energy upon my enemies.*  \n- **Summon Demon**: Call forth a loyal servant to fight by my side.  \n- `Soulstone`: *Cheat death itself.*  ")
        true_blocks.append("> *\"Power comes at a price, but it's a price I'm willing to pay.\"* – **Ward Rackley**")
        true_blocks.append("---")
        true_blocks.append("## Places I've Conquered  ")
        true_blocks.append("- [Scarlet Monastery](https://wowpedia.fandom.com/wiki/Scarlet_Monastery): A den of zealots who fell to my fire and shadow.  \n- [Burning Steppes](https://wowpedia.fandom.com/wiki/Burning_Steppes): *Where the ground burns as fiercely as my soul.*  ")
        true_blocks.append("![Ward Rackley in Action](https://via.placeholder.com/800x400.png)")
        true_blocks.append("---")
        true_blocks.append("## Pro Tips for Aspiring Warlocks  ")
        true_blocks.append("Here’s a bit of code to maximize your DPS rotation:")
        true_blocks.append("```\n/castsequence reset=target Corruption, Curse of Agony, Shadow Bolt\n```")

        self.assertEqual(blocks, true_blocks)

    
    def test_block_label(self):
        text = open("src/test_files/test_text_to_textnodes.md" , "r").read()

        blocks = split_blocks(text)

        labels = list(map(label_block , blocks))

        true_block_labels = ([  BlockType.HEADER.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.PAR.value,
                                BlockType.ULIST.value,
                                BlockType.QUOTE.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.ULIST.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.PAR.value,
                                BlockType.CODE.value
        ])

        self.assertEqual(list(map(lambda l: l.value , labels)) , true_block_labels)

    def test_block_label2(self):
        text = open("src/test_files/test_to_html.md" , "r").read()

        blocks = split_blocks(text)

        labels = list(map(label_block , blocks))

        true_block_labels = ([  BlockType.HEADER.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.PAR.value,
                                BlockType.ULIST.value,
                                BlockType.QUOTE.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.OLIST.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.PAR.value,
                                BlockType.CODE.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value,
                                BlockType.HEADER.value,
                                BlockType.ULIST.value,
                                BlockType.ULIST.value,
                                BlockType.ULIST.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value,
                                BlockType.PAR.value

        ])


        self.assertEqual(list(map(lambda l: l.value , labels)) , true_block_labels)