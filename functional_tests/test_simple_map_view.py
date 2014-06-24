from base import FunctionalTest
from selenium import webdriver

class NewVisitorTest(FunctionalTest):

    def test_can_visit_home_page_and_explore_trees(self):
        #Arlo has head about a cool new online treemap for toronto. He goes to checkout it's home page.
        self.browser.get(self.server_url)

        # He notices a nice intro page with a tree background image, as well as the page title and header mention toronto tree map.
        self.assertIn('Tree Map', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1'),text
        self.assertIn('Toronto Tree Map', header_text)

        # He is invited to click on a tree to see tree info.
        section_text = self.browser.find_element_by_id('id_tree_info')
        self.assertIn("click on a tree")