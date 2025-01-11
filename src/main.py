from markdown_to_html import markdown_to_html

from copy_dir import copy_dir
from convert_dir import convert_dir
def main():
    copy_dir()
    convert_dir()
    
    #in_file = open("src/test_files/test_to_html.md" , "r")
    #text = in_file.read()
    #in_file.close()

    #html = markdown_to_html(text)

    #out_file = open("src/test_files/test_output.html" , "w")
    #out_file.write(html.to_html())
    #out_file.close()


main()
