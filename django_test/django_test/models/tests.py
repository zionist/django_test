import re
from collections import OrderedDict
from django.test import TestCase, override_settings

from django_test.models.models import Category, Item
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
        Product.objects.create(name="product 6", price=100, category_id=3)
        Product.objects.create(name="product 7", price=98, category_id=3)
        Product.objects.create(name="product 8", price=100, category_id=3)
        Product.objects.create(name="product 9", price=100, category_id=3)
        Product.objects.create(name="product 10", price=100, category_id=3)
        Product.objects.create(name="product 11", price=100, category_id=3)
        Product.objects.create(name="product 12", price=100, category_id=3)
        Product.objects.create(name="product 13", price=100, category_id=3)
        Product.objects.create(name="product 14", price=100, category_id=3)
        Product.objects.create(name="product 15", price=100, category_id=3)
        Item.objects.create(name="item 1", active=True)
        Item.objects.create(name="item 2", active=True)

    def test_regex(self):
        """
        Написать код (с помощью регулярных выражений) для удаления из строки незакрытых скобок
        вместе с их содержимым, если после них нет закрытых блоков: 'asdfd((asdf)(asdf' -> 'asdfd((asdf)'
        """
        self.assertEquals(re.sub('\([^)]*$', '', 'asdfd((asdf)(asdf'), 'asdfd((asdf)')
        self.assertEquals(re.sub('\([^)]*$', '', 'asdfd((asdf)(asdf(sdsd(((dsds((('), 'asdfd((asdf)')

    def test_no_regex(self):
        """
        Написать код (без регялярных выражений) для удаления из строки незакрытых скобок
        вместе с их содержимым, если после них нет закрытых блоков: 'asdfd((asdf)(asdf' -> 'asdfd((asdf)'
        """
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
        self.assertEquals(do_test('asdfd((asdf)(asdf(sdsd(((ds!!!ssd321321s((('), 'asdfd((asdf)')

    @override_settings(DEBUG=True)
    def test1(self):
        """
        С помощью Django ORM выбрать товары, цена которых больше или равна 100 руб.,
        сгруппировать по категориям и посчитать количество товаров в каждой категории.
        """
        return
        # we want to use ordering categories by name
        result = OrderedDict()
        # select id and name from all Categories
        for cat in Category.objects.values('id', 'name').order_by('name'):
            result[cat['name']] = Product.objects.filter(category_id=cat['id'], price__gte=100)
        # select all related products. We need them all, so get them all and count len in memory.
        # Do not make additional count request
        print("\n")
        [print("Category %s. Count of products is %s" % (r, len(result[r]))) for r in result.keys()]
        self.assertEqual(len(result["cat1"]), 1)
        self.assertEqual(len(result["cat2"]), 1)
        self.assertEqual(len(result["cat3"]), 11)
        self.assertEqual(result["cat1"][0], Product.objects.get(name="product 2"))

    @override_settings(DEBUG=True)
    def test2(self):
        """
        С помощью Django ORM выбрать товары, цена которых больше или равна 100 руб.,
        сгруппировать по категориям и посчитать количество товаров в каждой категории.
        Оставить лишь категории, в которых строго больше 10 товаров
        """
        result = OrderedDict()
        for cat in Category.objects.values('id', 'name').order_by('name'):
            query = Product.objects.filter(category_id=cat['id'], price__gte=100)
            # make select count request. If count of category related products >10 then we can make select * request
            if query.count() > 10:
                result[cat['name']] = query
        # do requests
        print("\n")
        [print("Category with >= 10 products %s. Count of products %s" % (r, len(result[r]))) for r in result.keys()]
        self.assertEqual(len(result["cat3"]), 11)
        self.assertEqual(len(result.keys()), 1)
        self.assertIn(Product.objects.get(name="product 4"), result["cat3"])
        self.assertIn(Product.objects.get(name="product 15"), result["cat3"])

    @override_settings(DEBUG=True)
    def test3(self):
        """
        Написать код python, который выводит в консоль перечень всех товаров. Каждая строка должна содержать следующие данные:
        •    название категории товара,
        •    наименование товара,
        •    цена.
        По возможности, минимизировать количество обращений к базе данных и количество передаваемых данных
        """
        return
        products = Product.objects.values('name', 'category__name', 'price').order_by("category__name", "name")
        print("\n")
        [print("Name %s. Category %s. Price %d" % (p["name"], p["category__name"], p["price"])) for p in products]

    @override_settings(DEBUG=True)
    def test4(self):
        """
        Suppose we have model with a custom manager ...
        """
        # check CustomQuerySet works
        Item.objects.filter(pk=1).delete()
        self.assertEqual(Item.objects.get(pk=1).active, False)
        self.assertEqual(Item.objects.get(pk=2).active, True)
        # check real delete
        Item.objects.filter(pk=1).delete_real()
        # object must be deleted
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(pk=1)





