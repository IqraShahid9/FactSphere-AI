class PlannerAgent:
    def __init__(self):
        self.plan = []

    def create_plan(self, query):
        subtopics = query.split(" ")[:5]  # demo
        self.plan = subtopics
        return self.plan

    def assign_tasks(self, search_agent):
        tasks = []
        for topic in self.plan:
            tasks.append(search_agent.search(topic))
        return tasks
