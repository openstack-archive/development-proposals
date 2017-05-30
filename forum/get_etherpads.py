#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

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

