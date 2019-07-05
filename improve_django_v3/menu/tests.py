from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User 
from django.core.urlresolvers import reverse

from .models import Menu, Item, Ingredient

class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Chef1",
            email="chef1@example.com",
            password="123"
        )
        self.honey = Ingredient.objects.create(name="honey")
        self.ice = Ingredient.objects.create(name="ice")
        self.tea = Ingredient.objects.create(name="tea")

        self.ice_tea = Item.objects.create(
            name="Ice Tea",
            description="A delisious ice tea with honey",
            chef=self.user,
        )
        self.ice_tea.ingredients.add(self.honey, self.ice, self.tea)
        self.ice_tea.save()

    def test_ingredient_creation(self):
        pk_ingredient = self.tea.pk
        self.assertEqual(Ingredient.objects.filter(pk=pk_ingredient).exists(), True)
    
    def test_item_creation(self):
        pk_item = self.ice_tea.pk
        self.assertEqual(Item.objects.filter(pk=pk_item).exists(), True)

    def test_menu_creation(self):
        menu = Menu.objects.create(
            season="Coco Late"
        )
        menu.items.add(self.ice_tea)
        menu.save()
        pk_menu = menu.pk
        self.assertEqual(Menu.objects.filter(pk=pk_menu).exists(), True)

    def test_menu_contains_item(self):
            menu = Menu.objects.create(
                season="Ices fiber"
            )
            menu.items.add(self.ice_tea)
            menu.save()
            item = menu.items.all()[0]

            self.assertEqual(item, self.ice_tea)

class MenuViewsTests(TestCase):
    def setUp(self):
        self.user2 = User.objects.create(
            username="Chef2",
            email="chef2@example.com",
            password="1234"
        )
        self.honey = Ingredient.objects.create(name="honey")
        self.ice = Ingredient.objects.create(name="ice")
        self.tea = Ingredient.objects.create(name="tea")

        self.ice_tea = Item.objects.create(
            name="Ice Tea",
            description="A delisious ice tea with honey",
            chef=self.user2,
        )
        self.ice_tea.ingredients.add(self.honey, self.ice, self.tea)
        self.ice_tea.save()

        self.menu = Menu.objects.create(
            season="Teas cool"
        )
        self.menu.items.add(self.ice_tea)
        self.menu.save()

        self.menu2 = Menu.objects.create(
            season="Green sprint"
        )
        self.menu2.items.add(self.ice_tea)
        self.menu2.save()
    
    def test_menu_list_view(self):
        resp = self.client.get(reverse('menu_list'))
        self.assertEqual(resp.status_code, 200)
        menus = [menu for menu,_ in resp.context['menus']]
        self.assertIn(self.menu, menus)
        self.assertIn(self.menu2, menus)
        self.assertTemplateUsed(resp, 'menu/list_all_current_menus.html')
        self.assertContains(resp, self.menu.season)
    
    def test_menu_detail_view(self):
        resp = self.client.get(reverse('menu_detail',
                                       kwargs={'pk': self.menu2.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.menu2, resp.context['menu'])
    
    def test_item_detail_view(self):
        resp = self.client.get(reverse('item_detail',
                    kwargs={'pk': self.ice_tea.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.ice_tea, resp.context['item'])