#!/usr/bin/env python

import wikipedia
import sys
import request

from bs4 import BeautifulSoup

from urllib.parse import urljoin

def extract_links(url):

page=wikipedia.page(url)

links = []


for link in links:
	print link["page"]


for link in page.links:
	links.append({"text" link["page"],

	"href": link["page"]
	})
	return links


if__name__== "__main__":

	if len(sys.argv) != 2: 
		print("\nUsage:\n\t{} <URL>\n".format(sys.argv[0]))
		sys.exit(1)

for link in extract_links(sys.argv[-1]):
	print("[{}]({})".format(link["text"], link["href"]))


