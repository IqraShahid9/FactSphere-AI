class SynthesisAgent:
    def __init__(self):
        self.memory = {}

    def synthesize(self, search_results, query):
        summary = f"Summary for '{query}':\n"
        for res in search_results:
            summary += f"- {res}\n"
        self.memory[query] = summary
        return summary
