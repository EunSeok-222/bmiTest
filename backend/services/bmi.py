class BMICalculator:

    def __init__(self, weight: float, height: float):

        self.weight = weight
        self.height = height / 100

    def calculate_bmi(self) -> float:

        return self.weight / (self.height ** 2)

    def get_bmi_category(self) -> str:
        
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "저체중"
        elif bmi < 23:
            return "정상"
        elif bmi < 25:
            return "과체중"
        elif bmi < 30:
            return "비만"
        else:
            return "고도비만"

    def get_result(self) -> dict:
       
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()

        return {
            "bmi": round(bmi, 2),
            "category": category
        }
