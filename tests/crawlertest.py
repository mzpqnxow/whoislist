import unittest
from testcase import WhoisServersListTestCase
from fixtures.mock import UrlReaderMock
from whoislist.crawler import *
from whoislist.parser import WhoisServersListParser

class WhoisServersListCrawlerTest(WhoisServersListTestCase):

    def setUp(self):
        config = { "url" : "http://www.iana.org/domains/root/db" };
        self.crawler = WhoisServersListCrawler(UrlReaderMock(), WhoisServersListParser(), config);

    def test_getWhoisServersList_commonUse_sholdReturnListWithWhoisServers(self):
        whoisList = self.crawler.getWhoisServersList();
        expectedResult = [
            { "domain" : "ac", "whois": "whois.nic.ac" },
            { "domain" : "br", "whois": "whois.registro.br" },
        ];
        self.assertEqual(expectedResult, whoisList);

if __name__ == "__main__":
    unittest.main()
