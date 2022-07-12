import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    for xml_file in glob.glob(path + '/*.xml'):
        xml_list = []
        tree = ET.parse(xml_file)
        print("xml_file", xml_file.split('.')[0])
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text),
                     member[0].text
                     )
            xml_list.append(value)
        # column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        # column_name = ['filename', 'xmin', 'ymin', 'xmax', 'ymax', 'class']
        # xml_df = pd.DataFrame(xml_list, columns=column_name)
        xml_df = pd.DataFrame(xml_list)
        xml_df.reset_index(drop=True)
        # Writing dataframe to csv
        xml_file = xml_file.split('.')[0]
        xml_df.to_csv(f'{xml_file}.csv', index=None)


def main():
    xml_path = os.path.join(os.getcwd(), r'dataset/xml')
    xml_to_csv(xml_path)
    print('Successfully converted xml to csv')

main()