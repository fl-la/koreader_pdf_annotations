# Overview

**A short overview about my use-case:**

- I'm using koreader for reading (and highlighting!) academic papers for research (beside other pdf-readers on my PC like okular)
- I'm using jabref to organize my research and literature

With koreader I ran into the issue that:
- all highlights at another pdf-reader are black (and therefore the text cannot be read anymore)
- jabref is not able to read out the content of the highlights created with koreader (didn't spent time to search for the issue)

That's why I created this script doing the following:
- save a copy of the original pdf file (called .NAME_OF_THE_FILE.bak)
- remove all origin annotations created with koreader
- and write them back to the file (chaning all highlights (like underline/highlight) to highlight ones) with the relevant meta-informations

With this (simple) solution jabref is able to read annotations and okular/other pdf viewers printing the highlights well.
