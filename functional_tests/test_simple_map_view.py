from .base import FunctionalTest
from selenium import webdriver

class NewVisitorTest(FunctionalTest):

    def test_can_visit_home_page_and_explore_trees(self):
        #Arlo has head about a cool new online treemap for toronto. He goes to checkout it's home page.
        self.browser.get(self.server_url)

        # He notices a nice intro page with a tree background image, as well as the page title and header mention toronto tree map.
        self.assertIn('Tree Map', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Toronto tree map', header_text)

        # He is invited to click on a tree to see tree info.
        section_text = self.browser.find_element_by_class_name('intro-text').text
        self.assertIn("Click on a tree",section_text)

        # Arlo sees a map with a bunch of green trees appear. He clicks on a tree and the trees details appear in the side bar.

        # He wants to see what trees are around his house, so he clicks on the 'locate me' button, and the map zooms to his house on Fernwood park.