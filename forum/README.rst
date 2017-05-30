Working with ##hashtag Program
==============================

* Retrieve etherpad content

  $python get_etherpads.py

  This will download list of etherpads to local directory.
  Files are prefix with "PAD-<etherpad-name>".

* Generate ##hashtag result

  $python extract_tags.py

  This will read the content from the list of downloaded files
  from previous step, then extract the ##hashtag from each lines,
  and output to a list of "TAG-<##hashtag>.md".

