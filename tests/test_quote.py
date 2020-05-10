import unittest
from app.models import Quote

class QuoteTest(unittest.TestCase):
    """
    Test Class to test the behaviour of Quotes
    """

    def setUp(self):
        """
        Set up method that will run before very test
        """
        self.new_quote = Quote(3,"Bananas", "Overripe bananas make banana bread")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

    def test_correct_quote_init(self):
        """
        Test that confirms object is instantiated correctly
        """
        self.assertEqual(self.new_quote.id, 3)
        self.assertEqual(self.new_quote.author, "Bananas")
        self.assertEqual(self.new_quote.quote, "Overripe bananas make banana bread")

    