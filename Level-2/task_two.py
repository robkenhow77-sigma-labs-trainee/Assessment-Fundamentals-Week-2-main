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


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
