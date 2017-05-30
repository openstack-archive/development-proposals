#!/usr/bin/env python

import re
import os
import urllib2
import urllib

# remove previously downloaded files that prefix with 'PAD-'
def cleanup_files(dir_path):
  files_to_remove = [ f for f in os.listdir(dir_path) if f.startswith("PAD-") ]
  for f in files_to_remove:
    os.remove(f)

def run():
  dir_path = os.path.abspath('')

  cleanup_files(dir_path)

  # connect to a URL that contain list of etherpads
  wiki = urllib2.urlopen("https://wiki.openstack.org/wiki/Forum/Boston2017")

  # read html code
  html = wiki.read()

  # slice the needed section only
  start_index = html.index("Event intro")
  end_index = html.index("(old) Brainstorming");
  html = html[start_index:end_index]

  # use re.findall to get all the links
  links = re.findall('"(https?://.*?)"', html)

  for link in sorted(links):
    if "etherpad" in link:
      filename = "PAD-" + link.split('/')[-1]
      url = link + "/export/txt"
      
      urllib.urlretrieve(url, filename)
      
if __name__ == "__main__":
    run()

