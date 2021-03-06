import unittest
from qual_id.categories.vehicle import Vehicle
from test.utils.category_helper import CategoryHelper


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle()

    def test__get_values__is_valid(self):
        error_message = CategoryHelper.get_values_error_message(self.vehicle)
        self.assertTrue(error_message == "", error_message)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
