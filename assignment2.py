from functools import wraps

def report_style(style):

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)

            if style == "box":
                border = "=" * 50
                return f"{border}\n{content}\n{border}"

            elif style == "star":
                border = "*" * 50
                return f"{border}\n{content}\n{border}"

            else:
                return content

        return wrapper
    return decorator


class Report:
    template = "Default Report"

    def __init__(self, title, data):
        self.title = title
        self.data = data


    @classmethod
    def set_template(cls, template_name):
        cls.template = template_name

    
    def __str__(self):
        report = f"Template : {Report.template}\n"
        report += f"Title    : {self.title}\n"
        report += "-" * 40 + "\n"

        for key, value in self.data.items():
            report += f"{key:<15}: {value}\n"

        return report

  
    def __eq__(self, other):
        return self.title == other.title and self.data == other.data

    
    def __len__(self):
        return len(self.data)


class ReportGenerator:

    @staticmethod
    @report_style("box")
    def generate(report):
        return str(report)

    @staticmethod
    @report_style("star")
    def generate_star(report):
        return str(report)




Report.set_template("Sales Summary Report")

report1 = Report(
    "Monthly Sales",
    {
        "Revenue": "$25,000",
        "Orders": 320,
        "Profit": "$8,500"
    }
)

report2 = Report(
    "Employee Report",
    {
        "Employees": 45,
        "Departments": 5,
        "Projects": 12
    }
)

print(ReportGenerator.generate(report1))
print()

print(ReportGenerator.generate_star(report2))
print()

print("Number of fields in Report 1:", len(report1))
print("Reports Equal:", report1 == report2)