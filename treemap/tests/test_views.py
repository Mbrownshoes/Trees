from django.http import HttpRequest
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
User = get_user_model()
from django.test.client import Client
from treemap.models import Trees, Harbord
from treemap.views import map_page, detail

from treemap.utils import get_map_form

class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'treemap/map.html')


class DetailPageTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.username = 'agconti'
        self.email = 'test@test.com'
        self.password = 'test'        
        self.test_user = User.objects.create_user(self.username, self.email, self.password)
        login = self.client.login(username=self.username, password=self.password)
        self.assertEqual(login, True)

    def test_detail_page_uses_detail_template(self):
        test_tree = Trees.objects.create(common_nam='bla',address_po='1',address_fu='foo',objectid='1',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
        response = self.client.get('/city_trees.%d/' % (test_tree.id,))
        self.assertTemplateUsed(response, 'treemap/detail.html')

    def test_passes_correct_tree_to_template(self):
        correct_list = Trees.objects.create(common_nam='bla',address_po='1',address_fu='foo',objectid='1',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
        response = self.client.get('/city_trees.%d/' % (correct_list.id,))
        self.assertEqual(response.context['tree'], correct_list)

    def test_displays_tree_form(self):
        tree_ = Trees.objects.create(common_nam='bla',address_po='1',address_fu='foo',objectid='1',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
        response = self.client.get('/city_trees.%d/' % (tree_.id,))
        geometry_field = 'geom'
        form_class = get_map_form(tree_.id) 
        wkt = getattr(tree_, geometry_field)
        form = form_class({'geometry' : wkt})
        MapForm = form.__class__

        self.assertEqual(response.context['form'].__class__.__name__,MapForm.__name__)

    ## probably not working cause I'm not signed in!!! response.content [in shell]


    def test_doesnt_display_tree_if_not_sigend_in(self):
        correct_list = Trees.objects.create(common_nam='bla',address_po='1',address_fu='foo',objectid='21',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
        other_list = Trees.objects.create(common_nam='bla1',address_po='1',address_fu='foofoo',objectid='1',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')

        response = self.client.get('/city_trees.%d/' % (correct_list.id,))
        self.assertNotContains(response, other_list.common_nam)

    def test_displays_fields_for_only_that_tree(self):
        User.objects.create(email='a@b.com')
        correct_list = Trees.objects.create(common_nam='bla',address_po='1',address_fu='foo',objectid='21',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
        # self.client.login(username='mathewbrown', password='kopidulu')
        response = self.client.get('/city_trees.%d/' % (correct_list.id,))
        # print(response.content)
        self.assertContains(response, 'bla')


    


