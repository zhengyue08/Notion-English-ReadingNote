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
token = 'a290b78d99a7b343fe6c0c160189950f2566e64ee9be985c157bbe57e0741785603f254afc6d19b7d3c700f87e315c98830d3436f59d0898ac3ad743524999e76018354331b754880080f4ad5022'
client  = NotionClient(token_v2 = token)
page = client.get_collection_view("https://www.notion.so/454aab2c4a054fb5a69f6ff193c0e3d5?v=364ad471360d4def85f8d6da157474aa")


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




