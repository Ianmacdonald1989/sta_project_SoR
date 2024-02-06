# from flask import Flask, render_template
# import openpyxl
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     workbook = openpyxl.load_workbook("catalogue_database_2.xlsx")
#     sheet = workbook.active
#     data = []
#     for row in sheet.iter_rows():
#         data.append([cell.value for cell in row])
#     return render_template("index.html", data=data)
#
# if __name__ == "__main__":
#     app.run()
