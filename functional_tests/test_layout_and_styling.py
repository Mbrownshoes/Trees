from .base import FunctionalTest

class LaoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):
        #Arlo goes to the homepage
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        #He notices the title nicely centered
        heading = self.get_item_heading()
        self.assertAlmostEqual(
            heading.location['x'] + heading.size['width']/2,
            512,
            delta=5
            )
        #He notices a map and sees a bunch of green dots appear
        