import xml.etree.cElementTree as ET
import os

path_of_the_directory= r'<Mention text label path>'
print("Files and directories in a specified path:")

for filename in os.listdir(path_of_the_directory):
    file = os.path.join(path_of_the_directory,filename)
    if file.split(".")[1] == "txt":
        if os.path.isfile(file):
            print(file)
            f = open(file, "r")
            root = ET.Element("annotation")
            Lines = f.readlines()
            for line in Lines:
                object = line.strip()
                object = object.strip("\n")
                object = object.split(" ")
                print("object", int(object[0]))
                print(f"{object[1], object[2], object[3], object[4]}")
                encoded_value = int(object[0])
                if encoded_value == 0:
                    label = "cat"
                elif encoded_value == 1:
                    label = "dog"
                elif encoded_value == 2:
                    label = "pig"
                elif encoded_value == 3:
                    label = "cow"
                elif encoded_value == 4:
                    label = "bird"
                else:
                    label = "insect"

                xml_object = ET.SubElement(root, "object")
                ET.SubElement(xml_object, "name").text = label
                filename = file.split(".")[0]
                ET.SubElement(xml_object, "filename").text = filename.rsplit("\\", 1)[1] + ".jpg"
                cordinates = ET.SubElement(xml_object, "bndbox")
                ET.SubElement(cordinates, "xmin").text = object[1]
                ET.SubElement(cordinates, "ymin").text = object[2]
                ET.SubElement(cordinates, "xmax").text = object[3]
                ET.SubElement(cordinates, "ymax").text = object[4]
                tree = ET.ElementTree(root)

                tree.write(f"{filename}.xml")
            f.close()


