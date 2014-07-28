from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.test import TestCase

from treemap.models import Trees, Harbord

class TreesModelTest(TestCase):
   
    def test_default_common_nam(self):
        tree = Trees()
        self.assertEqual(tree.common_nam, '')

    def test_cannot_save_empty_tree(self):
        tree = Trees(common_nam='')
        with self.assertRaises(ValidationError):
            tree.full_clean()

    def test_dublicate_trees_are_invalid(self):
        tree_ = Trees.objects.create(common_nam='bla',address_po='1',address_fu='foo',objectid='1',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
        with self.assertRaises(ValidationError):
            tree = Trees(common_nam='bla',address_po='1',address_fu='foo',objectid='1',struct_id='1',botanical_field='bar',diameter_b='1',tree_posit='1',geom='MULTIPOINT(-1.464854 52.561928)')
            tree.full_clean()


class HarbordModelTest(TestCase):
   
    def test_default_CommonSpeciesNames(self):
        harbord = Harbord()
        self.assertEqual(harbord.CommonSpeciesNames, '')

    def test_cannot_save_empty_tree(self):
        harbord = Harbord(CommonSpeciesNames='')
        with self.assertRaises(ValidationError):
            harbord.full_clean()

    def test_dublicate_trees_are_invalid(self):
        harbord_ = Harbord.objects.create(CommonSpeciesNames='bla',Street='foo',HouseNumber='1',Circumference='1',DBH='1',point='POINT(-1.464854 52.561928)')
        with self.assertRaises(ValidationError):
            harbord = Harbord(CommonSpeciesNames='bla',Street='foo',HouseNumber='1',Circumference='1',DBH='1',point='POINT(-1.464854 52.561928)')
            harbord.full_clean()
