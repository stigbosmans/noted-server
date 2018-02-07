class Page:
    def __init__(self, notebook, name, content):
        self.notebook = notebook
        self.name = name
        self.content = content
        self.create(name, content)

    def create(self, name, content):
        self.page_path = "{}/{}.md".format(self.notebook.get_path(), name)
        page = open(self.page_path, "w")
        page.write(content)
        page.close()