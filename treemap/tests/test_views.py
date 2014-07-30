from django.http import HttpRequest
from django.test import TestCase

from treemap.models import Trees, Harbord
from treemap.views import map_page, detail

from treemap.utils import get_map_form



class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'treemap/map.html')


class DetailPageTest(TestCase):

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
        form_class = get_map_form(tree_.id) 
        geometry_field = 'geom'
        wkt = getattr(tree_, geometry_field)
        form = form_class({'geometry' : wkt})
        self.assertIsInstance(response.context['form'], {'form' : form})

