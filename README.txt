September 3rd, 2023
By: Matthew Chen

This program requires a Python version of 2.5 or greater due to using the ElementTree library.
Run the code with python xml_leaf_highlighter.py [directory] in the terminal.
For example, with file names from the ZIP file sent in the assignment,
you'd run "python xml_leaf_highlighter.py Programming-Assignment-Data". 
The directory should contain all the XML files and screenshots.
My program assumes that every XML file has exactly 1 PNG file corresponding to it with the same name.
Output files will be in the directory highlighted_screenshots, which the program will create 
if it doesn't already exist. Existing files will be overwritten.

I chose to program this in Python because I have the most experience with this language.
In addition, I chose to use a recursive function instead of an iterative one to find the leaf nodes 
because otherwise extra storage would be needed for various lists to hold information. 
Finally, I chose to use ElementTree because it comes with Python and thus doesn't require any new modules. 
