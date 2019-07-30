import unittest
from app.models import Articles

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        
        '''
        Set up method that will run before every Test
        new instance below, to test,
        '''


        self.new_article = Articles('bbc','Trump dies in plane crash','joeReporter','21-04-2019','url','Poets on the verge of distinction')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

