import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(1,'Engadget', 'JOn Fingas', 'If you missed the sale earlier this month, nows your chance to grab Apples Mac Mini M1 at its best price yet. The compact desktop has returned to a record low of $570, thanks to a discount and a coupon that knocks an additional $80 off the sale price. Youl…','https://www.engadget.com/apples-mac-mini-m1-drops-back-down-to-an-all-time-low-of-570-135002983.html', '2022-03-01T21:07:48Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

if __name__ == '__main__':
    unittest.main()