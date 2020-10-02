import json
import webbrowser
from urllib import request


class BookFinder:

    def searchRequest(topics, maxR, orderType):

        baselink = "https://www.googleapis.com/books/v1/volumes?q=placeholderTopics"
        endlink = "&filter=ebooks&langRestrict=English&maxResults=placeholderMR&orderBy=placeholderOB&printType=BOOKS&projection=LITE"

        baselinkref = baselink.replace(
            'placeholderTopics', topics.lower().strip())
        endlinkref = endlink.replace('placeholderMR', str(maxR))
        endlinkref2 = endlinkref.replace('placeholderOB', orderType.lower())

        fullLink = baselinkref + endlinkref2

        with request.urlopen(fullLink) as f:
            text = f.read()

        decoded_text = text.decode("utf-8")
        objr = json.loads(decoded_text)

        return objr

    def openBookInfo(link):
        webbrowser.open(link)

    def downloadRequest(name):
        link = f"http://libgen.rs/search.php?req={name}&lg_topic=libgen&open=0&view=simple&res=25&phrase=1&column=def"
        webbrowser.open(link)
