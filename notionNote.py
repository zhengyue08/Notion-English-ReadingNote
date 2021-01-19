from notion.client import NotionClient
from notion.block import *
from bs4 import BeautifulSoup
import os
import loadclip
import getMean

# Prepare
token = 'a290b78d99a7b343fe6c0c160189950f2566e64ee9be985c157bbe57e0741785603f254afc6d19b7d3c700f87e315c98830d3436f59d0898ac3ad743524999e76018354331b754880080f4ad5022'
client  = NotionClient(token_v2 = token)
page = client.get_collection_view("https://www.notion.so/68b3dcbe6f374d8bbaa91c4325cbc8fd?v=d5786b87063348ea96ccff6bfde943f3")


# Add a new note to table
new = page.collection.add_row()
new.name = input("Please input the Title:\n")


# Open Clip File in Kindle
note_path='/Volumes/Kindle/documents/My Clippings.txt'
f=open(note_path,'r+')


# Fill content
new.children.add_new(SubheaderBlock,title = "MindMap")
new.children.add_new(DividerBlock)
WordsPharses = new.children.add_new(SubheaderBlock,title = "Wordsd/Phrases")


# Get Notes Words + Sentences
[words,sentences] = loadclip.note(f)

# Words Part
for word in words:
    toggleBlock = new.children.add_new(ToggleBlock,title = word)
    sen = getMean.mean(word)
    for item in sen:
        toggleBlock.children.add_new(BulletedListBlock,title = item.get_text())

new.children.add_new(DividerBlock)

# Words Part
new.children.add_new(SubheaderBlock,title = 'Inspirational Quotes')

for sentence in sentences:
    new.children.add_new(BulletedListBlock,title = sentence)




