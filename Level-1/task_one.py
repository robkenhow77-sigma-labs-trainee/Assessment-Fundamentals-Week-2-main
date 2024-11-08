from datetime import datetime, date


class Assessment:
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        if type not in ['multiple-choice', 'technical', 'presentation']:
            raise ValueError("Invalid assessment type")
        self.type = type
        if score > 100 or score < 0:
            raise ValueError("Invalid score")
        self.score = score



class Trainee:
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
        self.assessments.append(assessment)


    def get_assessment(self, name: str) -> Assessment | None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None





if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
