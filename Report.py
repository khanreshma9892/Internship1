import pandas as pd
from fpdf import FPDF

# Step 1: Read data
df = pd.read_csv("data.csv")

# Step 2: Basic analysis
average_score = df['Score'].mean()
max_score = df['Score'].max()
min_score = df['Score'].min()

# Step 3: Create PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Score Report", border=False, ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 10)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

    def add_summary(self, avg, max_, min_):
        self.set_font("Arial", size=12)
        self.cell(0, 10, f"Average Score: {avg:.2f}", ln=True)
        self.cell(0, 10, f"Highest Score: {max_}", ln=True)
        self.cell(0, 10, f"Lowest Score: {min_}", ln=True)
        self.ln(10)

    def add_table(self, dataframe):
        self.set_font("Arial", "B", 12)
        self.cell(60, 10, "Name", 1)
        self.cell(40, 10, "Score", 1)
        self.ln()

        self.set_font("Arial", size=12)
        for index, row in dataframe.iterrows():
            self.cell(60, 10, str(row["Name"]), 1)
            self.cell(40, 10, str(row["Score"]), 1)
            self.ln()

# Generate PDF
pdf = PDFReport()
pdf.add_page()
pdf.add_summary(average_score, max_score, min_score)
pdf.add_table(df)

pdf.output("score_report.pdf")
print("PDF report generated: score_report.pdf")
