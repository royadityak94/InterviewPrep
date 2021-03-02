''' Web Crawler
Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl. Return all urls obtained by your web crawler in any order. Your crawler should:
    = Start from the page: startUrl
    = Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
    = Do not crawl the same link twice.
    = Explore only the links that are under the same hostname as startUrl.

Reference: https://leetcode.com/problems/web-crawler/
'''
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_domain_name(url: str) -> str:
            return url.split('/')[2]
        if not startUrl:
            return []
        parent_domain = get_domain_name(startUrl)
        visited = {startUrl}
        output = [startUrl]
        queue = deque([startUrl])

        while queue:
            popped = queue.popleft()
            for child in htmlParser.getUrls(popped):
                if child in visited or get_domain_name(child) != parent_domain:
                    continue
                visited.add(child)
                queue += child,
                output += child,
        return output
