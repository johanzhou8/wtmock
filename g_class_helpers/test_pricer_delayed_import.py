from unittest import TestCase, mock, expectedFailure
# not importing `pricer`

class TestCountryPrices(TestCase):

    @expectedFailure
    def test_delayed_import(self):
        with mock.patch('pricer.COUNTRIES', ['GB']):
            from g_class_helpers.pricer import CountryPricer
            pricer = CountryPricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100, 'GB'), 80)
