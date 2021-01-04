#!/usr/bin/env python3

# script to make annotations added with koreader to pdfs readable in other pdf viewers like okular (or extracted through jabref)

import fitz
import sys
import urllib
import os

author = "florian"

class annotation:
    def __init__(self, quad, annotation):
        self.quad = quad
        self.annotation = annotation

def main():
    input_filename = sys.argv[1]
    doc = fitz.open(input_filename)
    doc.save("." + input_filename + ".bak")  #saving a backup of the original file
    page_count = doc.pageCount
    for page in range(page_count):
        print("Edit annotations at page ", page+1)
        pag = doc.loadPage(page)
        annotations = []
        for annot in pag.annots():
            ann = annotation(annot.rect.quad, annot)
            annotations.append(ann)  #save the quad for each annotation
            pag.deleteAnnot(annot)
            annot.delete_responses()
            annot.update()
        for annot in annotations:
            new_annot = pag.addHighlightAnnot(annot.quad)
            info = new_annot.info
            info["author"] = author
            info["content"] = annot.annotation.info["content"]
            info["subject"] = annot.annotation.info["subject"]
            info["modDate"] = annot.annotation.info["modDate"]
            info["creationDate"] = annot.annotation.info["creationDate"]
            info["title"] = annot.annotation.info["title"]
            info["id"] = annot.annotation.info["id"]
            new_annot.set_info(info)
            new_annot.update()

    doc.saveIncr()
    doc.close()

if __name__ == "__main__":
    main()