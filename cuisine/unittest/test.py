from django.test import TestCase

from cuisine.models import Cuisine, Dishes


class CuisineTest(TestCase):

    def test_create_cuisine(self):
        cuisine = Cuisine.objects.create(type_name='test1')
        self.assertIsNotNone(cuisine)
        self.assertEqual(cuisine.type_name, 'test1')

    def test_create_dishes(self):
        cuisine = Cuisine.objects.create(type_name='test1')
        self.assertIsNotNone(cuisine)
        dishes = Dishes.objects.create(
            cuisine_id=cuisine.id,
            desc='Just test 1'
        )
        self.assertIsNotNone(dishes)
        self.assertEqual(dishes.desc, 'Just test 1')

    def test_delete(self):
        cuisine = Cuisine.objects.create(type_name='test1')
        self.assertIsNotNone(cuisine)
        Dishes.objects.create(cuisine_id=cuisine.id, desc='Just test 1')
        Cuisine.objects.filter(type_name='test1').delete()
        dishes = Dishes.objects.select_related('cuisine').filter(cuisine__type_name='test1').first()
        self.assertIsNone(dishes)
