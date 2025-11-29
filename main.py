from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.synthesis_agent import SynthesisAgent
from agents.evaluator_agent import EvaluatorAgent
from tools.memory_tool import save_memory, load_memory

def main():
    query = input("Enter your research query: ")

    memory = load_memory()
    if query in memory:
        print("Found in memory:\n", memory[query])
        return

    planner = PlannerAgent()
    search_agent = SearchAgent()
    synthesis_agent = SynthesisAgent()
    evaluator = EvaluatorAgent()

    plan = planner.create_plan(query)
    print("Plan created:", plan)

    search_results = planner.assign_tasks(search_agent)
    print("Search Results:", search_results)

    summary = synthesis_agent.synthesize(search_results, query)
    print("Summary:\n", summary)

    save_memory(query, summary)

    evaluation = evaluator.evaluate(summary)
    print("Evaluation:", evaluation)

if __name__ == "__main__":
    main()
