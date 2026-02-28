class Report:
    def __init__(self, data):
        self.data = data

    def generate(self):
        return f"Reporte: {self.data}"

class ReportSaver:
    def save(self, content, filename):
        with open(filename, "w") as f:
            f.write(content)

if __name__ == "__main__":
    report = Report("Ventas 2026")
    saver = ReportSaver()
    saver.save(report.generate(), "reporte.txt")
