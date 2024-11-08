"""Datetime module"""
from datetime import date, datetime


class Assessment:
    """Assessment class"""
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        if type not in ['multiple-choice', 'technical', 'presentation']:
            raise ValueError("Invalid assessment type")
        self.type = type
        if score > 100 or score < 0:
            raise ValueError("Invalid score")
        self.score = score


class Trainee:
    """Trainee class"""
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []


    def get_age(self) -> int:
        """returns the age of the trainee in years"""
        year_difference = int(datetime.now().year) - int(self.date_of_birth.year)
        month_difference = int(datetime.now().month) - int(self.date_of_birth.month)
        day_difference = int(datetime.now().day) - int(self.date_of_birth.day)
        if month_difference >= 0:
            if day_difference >= 0:
                return year_difference
        return year_difference - 1


    def add_assessment(self, assessment: Assessment) -> None:
        """adds an assessment object to assessment list"""
        if not isinstance(assessment, Assessment):
            raise TypeError("Invalid object")
        self.assessments.append(assessment)


    def get_assessment(self, name: str) -> Assessment | None:
        """returns an assessment object if it is in the assessment list otherwise returns none"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """returns a list of assessments of a specific type"""
        return [assessment for assessment in self.assessments if assessment.type == type]


class MultipleChoiceAssessment(Assessment):
    """Multiple choice class"""
    def __init__(self, name, score):
        super().__init__(name = name, score = score, type = "multiple-choice")


    def calculate_score(self) -> float:
        """Returns the adjusted assessment score"""
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """technical Assessment class"""
    def __init__(self, name, score):
        super().__init__(name = name, score = score, type = "technical")


    def calculate_score(self) -> float:
        """Returns the adjusted assessment score"""
        return self.score


class PresentationAssessment(Assessment):
    """Multiple choice class"""
    def __init__(self, name, score):
        super().__init__(name = name, score = score, type = "presentation")


    def calculate_score(self) -> float:
        """Returns the adjusted assessment score"""
        return self.score * 0.6


class Question:
    """Question class"""
    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


class Quiz:
    """Quiz class"""
    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:
    """Marking class"""
    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz


    def mark(self) -> int:
        """Returns the quiz mark as a percentage"""
        marks = [True if q.chosen_answer == q.correct_answer else False for q in self._quiz.questions]
        if len(self._quiz.questions) <= 0:
            return 0
        return round( ( marks.count(True) / len(marks) ) * 100 )


    def generate_assessment(self) -> Assessment:
        """Creates an assessment object based on the quiz type and score"""
        type_of_quiz = self._quiz.type
        quiz_name = self._quiz.name
        score = self.mark()
        if type_of_quiz == 'multiple-choice':
            return MultipleChoiceAssessment(quiz_name, score)
        if type_of_quiz == 'technical':
            return TechnicalAssessment(quiz_name, score)
        if type_of_quiz == 'presentation':
            return PresentationAssessment(quiz_name, score)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    mark = Marking(quiz)
    print(mark.generate_assessment().score)

    questions = [
            Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
            Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
            Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
            Question("What is 4 + 4? A:2 B:4 C:5 D:8", "X", "."),
            Question("What is 5 + 5? A:10 B:4 C:5 D:8", "X", "."),
        ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
    marking = Marking(quiz)
    print(marking.generate_assessment().score)
