from fpdf import FPDF


class Bill:

    def __init__(self, amount: int, period: str):
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name: str, days_in_house: int):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill: Bill, flatmate2):
        total_days = self.days_in_house + flatmate2.days_in_house
        coefficient: float = self.days_in_house / total_days
        return bill.amount * coefficient


class PdfReport:

    def __init__(self, filename: str):
        self.filename = filename
        self.report = FPDF(orientation='P', unit='pt', format='A4')

    def generate(self, flatmate1: Flatmate, flatmate2: Flatmate, bill: Bill):
        self.report.add_page()
        # add house.png
        self.report.image("house.png", w=30, h=30)
        self.report.set_font(family='Times', size=24, style='B')
        self.report.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        self.report.set_font(family="Times", size=14, style='B')
        self.report.cell(w=100, h=40, txt="Period:", border=0)
        self.report.cell(w=150, h=40, txt=bill.period, align="R", border=0, ln=1)
        self.report.set_font(family="Times", size=12)
        self.report.cell(w=100, h=25, txt=flatmate1.name, border=0)
        self.report.cell(w=150, h=25, txt=str(round(flatmate1.pays(bill, flatmate2), 2)),
                         align="R", border=0, ln=1)
        self.report.cell(w=100, h=25, txt=flatmate2.name, border=0)
        self.report.cell(w=150, h=25, txt=str(round(flatmate2.pays(bill, flatmate1), 2)),
                         align="R", border=0, ln=1)
        self.report.set_font(family="Times", size=14, style='B')
        self.report.cell(w=100, h=25, txt="Total:", border=0)
        self.report.cell(w=150, h=25, txt=str(round(bill.amount, 2)), align="R", border=0, ln=1)

        self.report.output(self.filename)


def main() -> None:
    print('Hello World!')
    the_bill = Bill(amount=124, period="December 2020")
    print(f"The bill amount for {the_bill.period} is {the_bill.amount}")
    flatmate1 = Flatmate(name="John", days_in_house=20)
    flatmate2 = Flatmate(name="Jane", days_in_house=17)
    print(f"{flatmate1.name} stayed {flatmate1.days_in_house} days and pays: ",
          flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
    print(f"{flatmate2.name} stayed {flatmate2.days_in_house} days and pays: ",
          flatmate2.pays(bill=the_bill, flatmate2=flatmate1))
    pdf_report: PdfReport = PdfReport(filename=f"{the_bill.period}.pdf")
    pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)


if __name__ == "__main__":
    main()
