class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

airline_survey = Survey(
    "Airline Airlines Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Did you enjoy your flight with Airline Airlines?"),
        Question("Did you feel you were provided enough assistance when needed? If not, why?"),
        Question("Did you feel safe and confortable on your flight at Airline Airlines. If not, why?",
                 ["Yes", "No"], allow_text=True),
        Question("How would you rate your overall experience at Airline Airlines and why?",
                 ["Very good", "Good","Nuetral", "Bad", "Very Bad"], allow_text=True),
    ]
)

surveys = {
    "Satisfaction": satisfaction_survey,
    "Personality": personality_quiz,
    "Airline": airline_survey,
}