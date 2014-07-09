from functional_tests.base import FunctionalTest

class LaoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #Arlo goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        #He notices the title nicely centered
        