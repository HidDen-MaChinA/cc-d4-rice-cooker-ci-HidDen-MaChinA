import unittest
from rice_cooker.rice_cooker_main import RiceCooker

class TestRiceCooker(unittest.TestCase):
    def setUp(self):
        self.to_test = RiceCooker()
    def test_plug_in_that_rice_cooker(self):
        expect = "Oke now it's plugged in"
        self.assertEqual(self.to_test.plug_in_or_out_that_rice_cooker(),expect)
    def test_plug_out_that_rice_cooker(self):
        expect = "Oke now we removed the plug"
        self.to_test.plug_in_or_out_that_rice_cooker()
        self.assertEqual(self.to_test.plug_in_or_out_that_rice_cooker(),expect)
    def test_add_in_some_food_to_cook(self):
        expect = "Added a food: foo"
        self.assertEqual(self.to_test.add_in_some_food_to_cook("foo"), expect)
    def test_add_in_some_food_fail(self):
        expect = "Oke bro...I don\'t know what you are cooking, but I don\'t think it\'s comestible"
        for i in range(20):
            self.to_test.add_in_some_food_to_cook(f"food: {i}")
        self.assertEqual(self.to_test.add_in_some_food_to_cook("last food"), expect)
    def test_list_each_food_inside(self):
        expect = "Each food inside the rice-cooker, even if you shouldn\'t"
        expect += " have more than rice in it:\nfood: 0\nfood: 1\nfood: 2"
        for i in range(3):
            self.to_test.add_in_some_food_to_cook(f"food: {i}")
        self.assertEqual(self.to_test.list_each_food_inside(), expect)
    def test_list_each_food_if_ther_is_no_food(self):
        expect = "Oke...you\'re dumb...or you are just...dumb...Oke...anyway "
        expect += "the rice-cooker is broken"
        self.assertEqual(self.to_test.throw_at_people(),expect)
        self.assertEqual(self.to_test.broken,True)
    def test_get_the_dish(self):
        expect = "Oke, here is your dish: my dish\nAnyway, I think all you should do with"
        expect += " a rice-cooker is...cook rice. If you wanted to cook some steak or "
        expect += "something like that inside of it, the only place you belong is in jail."
        self.assertEqual(self.to_test.get_the_dish("my dish"), expect)
if __name__ == "__main__":
    unittest.main()
