# wiki_connect_two_articles

This script finds connection between two articles on Wikipedia in 3 steps (if possible)

# How to set up

- download project files in a single folder
- install python 3+ if neccessary
- in python use this command: **pip install -r requirements**  (if any issues, install packages manually or use IDE and store all scripts in one project)
- run main.py in terminal

The script checks if there are links set in the settings.py, if no - asks for links in console. 

# Functions

**main**() - Runs all funcs one by one, prints steps.

**get_path**() - Finds path between two articles.

**is_target_page**(url: str) - Checks if the end_url is on a given page.

**get_page_valid_links**(url: str) - Returns list of links for a given wiki url.


# Example of settings.py

![image](https://user-images.githubusercontent.com/100962655/224496458-263b4e9e-38e3-4a50-968d-911358b0d4a7.png)
