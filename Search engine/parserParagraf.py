# -*- coding: utf-8 -*-
import re
import os

from html.parser import HTMLParser


class ParserParagraf(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass
            
            

    def handle_data(self, data):
        stripped_text = re.sub('[\W]', ' ', data).split()
        if stripped_text:
            if self.lasttag == 'p':
                self.paragrafs.extend(stripped_text)
            self.words.extend(stripped_text)

    def parse(self, path):
        self.links = []
        self.words = []
        self.paragrafs = []

        try:
            with open(path, 'r', encoding= 'utf-8') as document:
                self.path_root = os.path.abspath(os.path.dirname(path))
                content = document.read()
                self.feed(content)
                self.links = list(set(self.links))

        except IOError as e:
            print(e)
        finally:
            return self.links, self.words, self.paragrafs   #
