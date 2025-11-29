from tools.search_tool import search_web

class SearchAgent:
    def __init__(self):
        pass

    def search(self, query):
        results = search_web(query)
        return results
