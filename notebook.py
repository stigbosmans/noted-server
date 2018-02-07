import os
from page import Page
class Notebook:
    notebook_path = "notebooks"
    pages = []
    def __init__(self, name):
        self.notebook_path = "{}/{}".format(self.notebook_path, name)
        if not os.path.exists(self.notebook_path):
            os.makedirs(self.notebook_path)

    def get_path(self):
        return self.notebook_path

    def add_page(self, page_name, page_content):
        page = Page(self, page_name, page_content)
        self.pages.append(page)