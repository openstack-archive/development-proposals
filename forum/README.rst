Working with ##hashtag Program
==============================

* Retrieve etherpads content 

  $python get_etherpads.py
  
  This will download the content of etherpads into local directory.
  Each file will be prefix with "PAD-<etherpad-links>"

* Generate report

  $python extract_tag.py

  This will extract all ##hashtag from the list of etherpad files downloaded
  in previous steps. The generated output will be saved in a list of files
  prefix with "TAG-<##hashtag>.md"


