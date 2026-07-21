import zipfile, xml.etree.ElementTree as ET, os, shutil

base_dir = r"c:\Study\TranAnhTu-workshop-main"
static_img_dir = os.path.join(base_dir, "static", "images", "5-Workshop")

os.makedirs(os.path.join(static_img_dir, "img_A"), exist_ok=True)
os.makedirs(os.path.join(static_img_dir, "img_B"), exist_ok=True)

def extract_and_copy_media(docx_file, subfolder):
    target_dir = os.path.join(static_img_dir, subfolder)
    with zipfile.ZipFile(os.path.join(base_dir, docx_file), 'r') as z:
        # read rels
        rels_xml = z.read('word/_rels/document.xml.rels')
        root_rels = ET.fromstring(rels_xml)
        rels_map = {}
        for child in root_rels:
            rid = child.attrib.get('Id')
            target = child.attrib.get('Target')
            if target and target.startswith('media/'):
                rels_map[rid] = os.path.basename(target)
                
        # extract media
        for f in z.namelist():
            if f.startswith('word/media/'):
                filename = os.path.basename(f)
                out_path = os.path.join(target_dir, filename)
                with open(out_path, 'wb') as out_f:
                    out_f.write(z.read(f))
    return rels_map

map_A = extract_and_copy_media('img_A.docx', 'img_A')
map_B = extract_and_copy_media('img_B.docx', 'img_B')

print("Extracted media successfully!")
print("Map A count:", len(map_A))
print("Map B count:", len(map_B))
