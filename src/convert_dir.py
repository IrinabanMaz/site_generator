import os
import shutil
from markdown_to_html import markdown_to_html, extract_title

def generate_page(from_path , template_path , dest_path):
    from_file = open(from_path , "r")
    md_text = from_file.read()
    title = extract_title(md_text)
    content = markdown_to_html(md_text).to_html()
    template_file = open(template_path , "r")
    html = template_file.read()
    html = html.replace("{{ Title }}" , title).replace("{{ Content }}" , content)

    dest_file = open(dest_path , "w")
    dest_file.write(html)
    dest_file.close()
    from_file.close()
    template_file.close()

def convert_dir(source = None , target = None):
    if source == None:
        src_directory = os.path.relpath("content")
    else:
        src_directory = source
    if target == None:
        tar_directory = os.path.relpath("public")
    else:
        tar_directory = target

    if not os.path.exists(tar_directory):
        os.mkdir(tar_directory)

    for item in os.listdir(src_directory):
        if os.path.isfile(os.path.join(src_directory ,item)):
            (head , tail) = os.path.splitext(item)
            if tail == ".md":
                generate_page(os.path.join(src_directory , item) , "template.html" , os.path.join(tar_directory, head + ".html"))
            else:
                shutil.copy(os.path.join(src_directory , item) , os.path.join(tar_directory , item))
        else:
            convert_dir(os.path.join(src_directory, item), os.path.join(tar_directory , item))
        
