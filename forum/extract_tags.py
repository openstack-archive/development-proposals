#!/usr/bin/env python
import re
import os

# remove all generated output file that begin with 'TAG' in filename
def cleanup_files(dir_path):
  files_to_remove = [ f for f in os.listdir(dir_path) if f.startswith("TAG") ]
  for f in files_to_remove:
    os.remove(f)

# read all files that begin with 'PAD' in filename
def get_files(dir_path):
  files = [f for f in os.listdir(dir_path) if f.upper().startswith("PAD")]
  # print files
  return sorted(files)

# write the generated output to a file, prefix with 'TAG' in filename
def write_md_report(hashtag, etherpad, text, line_number):
  with open ("TAG-" + hashtag + ".md", "a") as hashtag_file:
    hashtag_file.write('%s: %d: %s\n\n' %(create_link(etherpad), line_number, text))

# create the etherpad hyperlink
def create_link(etherpad):
  etherpad_link = "https://etherpad.openstack.org/p/" + etherpad 
  return etherpad_link

# skip all lines beginning with these words,
# which assumed to be the ##hashtag explanation notes
def skip_line(line):
  skip_words = [
  '##<hashtag>',
  '##hashtag',
  '##newfeature - Proposal for a new feature',
  '##gap - Feature gap that does not have a solution yet',
  '##uservoice - Feedback from users and operators',
  '##painpoint - Functional challenges/problems (either real or perceived)',
  '##<workload-type>',
  '##<project-name> ',
  '##<working-group/team-name>']

  for word in skip_words:
    if line.find(word) != -1:
      return 1

  return 0

# the main procedure
# 1. Cleanup previously generated files that prefix with 'TAG'
# 2. Read all files prefix with 'PAD'. 
#    These 'PAD' files are downloaded from 'get_etherpads.py'
# 3. For every lines in each PAD files, extract the ##hastag
# 4. Write the line with ##hashtag to a file 'TAG-<##hashtag>'
def run():  
  dir_path = os.path.abspath('')

  # Remove previously generated files
  cleanup_files(dir_path)

  hash_set = set([])

  rep_chars = ["##", ":", ",", "+1", "?", "<", ">", "(", ")"]  
  
  # read each etherpad content, line by line
  for file in get_files(dir_path):
    with open (file, 'rt') as f:
      line_number = 1

      for line in f:
        # trim whitespace characters
        line = line.strip()
        
        if skip_line(line) != 1:
          try:
            for hashtag in re.findall(r'#{2}\S*', line.lower()):
              # hack to workaround ##hashtag that was not properly formed
              # eg: '##something#action' instead of '##something #action' 
              # if hashtag.find('<') != -1:
              #   print hashtag
              for tag in hashtag.split('#'):
                for char in rep_chars:
                  tag = tag.replace(char, "").lower()
                
                if tag != "":
                  hash_set.add(tag)
                
                # the filename is the etherpad link that downloaded locally
                # prefix with 'PAD-'
                # simply replace 'PAD-' will give you the etherpad name
                write_md_report(tag, file.replace("PAD-",""), line,
                  line_number)

          except AttributeError:
            line = ""

        line_number += 1    

  print sorted(hash_set)

if __name__ == "__main__":
    run()

