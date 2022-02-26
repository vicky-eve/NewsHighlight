import unittest
from models import source , articles
Source = source.Source
Articles = articles.Articles

class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source("engadget","Engadget" , "Mat Smith", "The Morning After: The new phones of MWC 2022", "This morning is brought to you by a lot of phone news. To start, we’ve got our detailed review of Samsung’s Galaxy S22 (and S22 Plus) by the latest addition to Engadget’s editorial team, Sam Rutherford. We also have a first look at Oppo’s latest attempt at a …", "https://www.engadget.com/the-morning-after-the-new-phones-of-mwc-2022-121543081.html")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles("engadget","Engadget" , "Mat Smith", "The Morning After: The new phones of MWC 2022", "This morning is brought to you by a lot of phone news. To start, we’ve got our detailed review of Samsung’s Galaxy S22 (and S22 Plus) by the latest addition to Engadget’s editorial team, Sam Rutherford. We also have a first look at Oppo’s latest attempt at a …", "https://www.engadget.com/the-morning-after-the-new-phones-of-mwc-2022-121543081.html",  "https://s.yimg.com/os/creatr-uploaded-images/2022-02/1431fc02-955d-11ec-8cfa-4cd74fd58ee8", "2022-02-25T12:15:43Z", "This morning is brought to you by a lot of phone news. To start, weve got our detailed review of Samsungs Galaxy S22 (and S22 Plus) by the latest addition to Engadgets editorial team, Sam Rutherford.… [+4160 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
    unittest.main()