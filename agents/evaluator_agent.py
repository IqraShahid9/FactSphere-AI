class EvaluatorAgent:
    def __init__(self):
        pass

    def evaluate(self, summary):
        score = len(summary.split()) / 10
        feedback = "Looks good!" if score > 10 else "Needs more content"
        return {"score": score, "feedback": feedback}
