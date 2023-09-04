import os
import sys
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

"""
Goes through every XML file, finds the leaves, and annotates the screenshots
"""
def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Usage: python xml_leaf_highlighter.py directory")

    directory = sys.argv[1]

    # Create directory to hold the new screenshots if it doesn't already exist
    new_directory = "highlighted_screenshots"
    if not os.path.isdir(new_directory):
        os.mkdir(new_directory)

    xml_files, old_screenshots = extract_files(directory)

    # Iterate through the XML files and old screenshots simultaneously
    # Assumes every XML file has exactly 1 screenshot corresponding to it
    for i in range(len(xml_files)):
        xml_file = xml_files[i]

        # Try parsing XML file and tell user if it contains an error
        try:
            xml_tree = ET.parse(xml_file)
        except Exception as e:
            print(f"Error on {xml_file}:\t {e}")
            continue
        
        # Get root of XML tree and find its leaf nodes
        root_element = xml_tree.getroot()
        leaves = find_leaf_nodes(root_element)

        # Access screenshot
        screenshot_file = old_screenshots[i]
        screenshot = Image.open(screenshot_file)
        ss_draw = ImageDraw.Draw(screenshot)
        
        # Go through each leaf node and draw on screenshot
        for leaf in leaves:
            corners = []
            
            # Finds corner from the XML file in the format [0, 0][0, 0]
            messy_corners = leaf.attrib["bounds"].split(",")

            # Extracts the digits from the messy_corners 
            corners.append(int(messy_corners[0].replace("[", "")))
            corners.append(int(messy_corners[1].split("]")[0]))
            corners.append(int(messy_corners[1].split("[")[1]))
            corners.append(int(messy_corners[2].replace("]", "")))
            
            # Draw the rectangle
            ss_draw.rectangle(tuple(corners), outline="yellow", width=10)
        
        # Save the screenshot to the new directory
        screenshot.save(os.path.join(new_directory, "highlighted." + screenshot_file.split(os.sep)[1]))

"""
Recursively finds leaf nodes of the node given
Parameter: Node element
Return: List with all leaf nodes
"""
def find_leaf_nodes(node):
    leaf_nodes = []

    # If node has children, check each of them for leaf nodes
    if len(node) > 0:
        for child in node:
            leaf_nodes += find_leaf_nodes(child)
    # Otherwise, add them to list of leaf nodes
    else:
        leaf_nodes.append(node)
        return leaf_nodes
    
    return leaf_nodes

"""
Gets the XML and screenshot files from the directory given
Parameters: Directory name, string
Return: Nested list with first list containing XML file names 
and second list containing screenshot file names
"""
def extract_files(directory):
    # List with xml and screenshot file names
    xml_and_screenshot_list = [[], []]

    # Iterate through each file in the directory
    for entry in os.scandir(directory):
        file = entry.path
        if file.endswith(".xml"):
            xml_and_screenshot_list[0].append(file)
        elif file.endswith(".png"):
            xml_and_screenshot_list[1].append(file)

    return xml_and_screenshot_list

if __name__ == "__main__":
    main()