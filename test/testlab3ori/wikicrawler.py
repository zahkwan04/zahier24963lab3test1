#!/usr/bin/env python
import wikipedia
import sys


page = wikipedia.page(sys.argv[-1])
links = []

for link in page.links:
        links.append({"page":link})

for link in links:
        print(link["page"])