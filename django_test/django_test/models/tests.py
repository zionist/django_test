import sys
import re

from django.test import TestCase, override_settings
from django_test import settings

from django_test.models.models import Category
from django_test.models.models import Product


class TaskCaseTest(TestCase):

    def setUp(self):
        Category.objects.create(name="cat1")
        Category.objects.create(name="cat2")
        Category.objects.create(name="cat3")
        Product.objects.create(name="product 1", price=99, category_id=1)
        Product.objects.create(name="product 2", price=101, category_id=1)
        Product.objects.create(name="product 3", price=102, category_id=2)
        Product.objects.create(name="product 4", price=103, category_id=3)
        Product.objects.create(name="product 5", price=104, category_id=3)
        Product.objects.create(name="product 6", price=99, category_id=3)
        Product.objects.create(name="product 7", price=98, category_id=3)

    def test_regex(self):
        self.assertEquals(re.sub('\([^)]*$', '', 'asdfd((asdf)(asdf'), 'asdfd((asdf)')
        self.assertEquals(re.sub('\([^)]*$', '', 'asdfd((asdf)(asdf(sdsd(((dsds((('), 'asdfd((asdf)')

    def test_no_regex(self):
        def do_test(s):
            idx = 0
            del_idx = None
            for c in s:
                    idx += 1
                    if c == '(':
                        if not del_idx:
                            del_idx = idx
                    elif c == ')':
                        del_idx = None
            if del_idx:
                s = s[:del_idx - 1]
            return s
        self.assertEquals(do_test('asdfd((asdf)(asdf'), 'asdfd((asdf)')
        self.assertEquals(do_test('asdfd((asdf)(asdf(sdsd(((dsds((('), 'asdfd((asdf)')

    # @override_settings(DEBUG=True)
    def test1(self):
        """
        С помощью Django ORM выбрать товары, цена которых больше или равна 100 руб.,
        сгруппировать по категориям и посчитать количество товаров в каждой категории.
        """
        return
        result = {}
        # select id and name from all Categories
        for cat in Category.objects.values('id', 'name'):
            result[cat['name']] = Product.objects.filter(category_id=cat['id'], price__gte=100)
        # select all related products. We need them all, so count len in memory do not make additional count request
        [print("Category %s. Count of products %s" % (r, len(result[r]))) for r in result.keys()]

    @override_settings(DEBUG=True)
    def test2(self):
        return
        cats = [c for c in Category.objects.values('id', 'name')]
        result = {}
        for cat in cats:
            query = Product.objects.filter(category_id=cat['id'], price__gte=10)
            # make select count request. If count of category related products >=10 then we can make select * request
            if query.count() == 1:
                result[cat['name']] = query
        print(result)
        [print("Category with >= 10 products %s. Count of products %s" % (r, len(result[r]))) for r in result.keys()]
        settings.DEBUG = False



