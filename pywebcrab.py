#!/usr/bin/env python3
# coding:utf-8

""" PyWebCraB - Python Web Crawler Bot """

__author__       = "Toropov Ivan (iwi(at)hotmail(dot)it)"
__copyright__    = "Copyright (C) 2014 netquote.it"
__license__      = "GPL 3.0"

__version_info__ = ('0', '0', '5')
__version__      = '.'.join(__version_info__)

import mechanize
from BeautifulSoup import BeautifulSoup

def main():
    url = 'https://www.deviantart.com/'
    browser = mechanize.Browser()
    browser.addheaders = [('User-agent', 'Firefox')]
    response = browser.open(url)
    soup = BeautifulSoup(response.read())
    image_tags = soup.findAll('img')
    for image in image_tags:
        print('{}'.format(image['src']))

if __name__ == "__main__":
    # Main function
    main()
