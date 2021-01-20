from notion.client import NotionClient
from notion.block import *
from bs4 import BeautifulSoup
import os
import loadclip
import getMean


# Open Clip File in Kindle
note_path='/Volumes/Kindle/documents/My Clippings.txt'
f=open(note_path,'r+')

# Get Notes Words + Sentences
[words,sentences] = loadclip.note(f)

f.seek(0)
f.truncate()    # Clean the .txt file
f.close()

# Prepare
token = '<input your token>'
client  = NotionClient(token_v2 = token)
page = client.get_collection_view("<input your address>")


# Add a new note to table
new = page.collection.add_row()
new.name = input("Please input the Title:\n")


# Fill content
new.children.add_new(SubheaderBlock,title = "MindMap")
new.children.add_new(DividerBlock)
WordsPharses = new.children.add_new(SubheaderBlock,title = "Wordsd/Phrases")



# Words Part
for word in words:
    toggleBlock = new.children.add_new(ToggleBlock,title = word)
    sen = getMean.mean(word)
    for item in sen:
        toggleBlock.children.add_new(BulletedListBlock,title = item.get_text())

new.children.add_new(DividerBlock)

# Sentences Part
new.children.add_new(SubheaderBlock,title = 'Inspirational Quotes')

for sentence in sentences:
    new.children.add_new(BulletedListBlock,title = sentence)




