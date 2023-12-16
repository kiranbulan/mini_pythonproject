"""
Name: Kiran Bulan
From: Nepal
project name: Student Report Card

"""
import csv
from tabulate import tabulate
from datetime import date
from fpdf import FPDF
pdf = FPDF()


def main():
    user_name = name_major(input("Student Name: ").strip())
    user_num = symbol_num(int(input("Symbol no: ")))
    user_major = name_major(input("Major: ").strip())
    suject_num = int(input("Number of suject: "))
    std_info = students_mark(suject_num)
    rlt = result(std_info)
    today = date.today()

    #print all detail of student
    print("\n")
    print(15 * " " + "REPORT CARD")
    print(f"Name: {user_name}        Publich Date: {today}")
    print(f"Major: {user_major}     symbol no: {user_num}")
    print(f"Result: {rlt} \n")
    print(10 * " " + "Grade/Mark-Sheet" + 10 * " ")
    print(f"{marksheet(std_info)}")


    #creating pdf file
    pdf.add_page()
    header()
    info_section(user_name, today, user_major,  user_num, rlt)
    creating_table()
    pdf.output(f"{user_name}.pdf")


#check user_input
def name_major(s):
    if not s or s.isnumeric():
        raise ValueError
    else:
        return s.title()

#check for user symbol
def symbol_num(n):
    if n in range(100000):
        return n
    else:
        raise ValueError

#provide grading according to obtain mark
def grading(subject):
    if subject <= 100 and subject >= 90:
        return "A+"
    elif subject <= 89 and subject >= 80:
        return "A "
    elif subject <= 79 and subject >= 70:
        return "B+"
    elif subject <= 69 and subject >= 60:
        return "B "
    elif subject <= 59 and subject >= 50:
        return "C+"
    elif subject <= 49 and subject >= 40:
        return "C "
    elif subject <= 39 and subject >= 20:
        return "D "
    elif subject <= 19 and subject >= 0:
        return "F "
    else:
        return "F "

#collects students subject and mark (subject: mark format)
def students_mark(num):
    subject_list = []
    for i in range(num):
        print("Subject: Marks ")
        subjects = input().split(":")
        grading_list = (
            [i + 1]
            + [subjects[0].title()]
            + [int(subjects[1])]
            + [grading(int(subjects[1]))]
        )
        subject_list.append(grading_list)
    return subject_list


#provide result according to obtain marked
def result(r):
    temp = []
    for i in range(0, len(r)):
        if "F" in r[i] or "F " in r[i]:
            temp.append("Failed")
        else:
            temp.append("passed")

    if "Failed" not in temp:
        return "Congratulation! You have Passed"
    else:
        return "Sorry! You have Failed"


#creating in table and insert std detail in csv file
def marksheet(m):
    my_list = m
    with open("std.csv", "w") as after_csv:
        writer = csv.writer(after_csv)
        header = ["S.N", "Subject", "Mark Obtain", "Grade"]
        writer.writerow(header)
        writer.writerows(my_list)
    return(tabulate(my_list, header, tablefmt="pretty"))


# header part of pdf file
def header():
    pdf.set_font("helvetica", "", 50)
    pdf.set_text_color(255,248,220)
    pdf.cell(190, 60, "REPORT CARD",border=1, new_x="LMARGIN",new_y="NEXT",align="C",fill=True,)
    pdf.ln(2)
    pdf.cell(190, 10, border=1,new_x="LMARGIN", new_y="NEXT",align="C",fill=True,)
    pdf.ln()


#body part of pdf file
def info_section(name, publish_date, major, symbol_no, result_msg):
    pdf.set_font("helvetica", "", 18)
    pdf.set_text_color(0, 0, 0)
    pdf.set_draw_color(0,0,0)
    pdf.cell(50, 20, f"Name: {name}", align="L")
    pdf.cell(130, 20, f"Publish date: {publish_date}", align="R")
    pdf.ln()
    pdf.cell(50, 5, f"Major: {major}", align="L")
    pdf.cell(120, 5, f"S.No: {symbol_no}", align="R")
    pdf.ln()
    pdf.cell(24, 20, "Result:", align="L")
    pdf.set_text_color(220,20,60)
    pdf.cell(0, 20, f"{result_msg}", )
    pdf.ln(15)


# # creating Styled table suing csv file
def creating_table():
    pdf.set_font("helvetica", "", size=20)
    pdf.set_text_color(0,0,0)
    pdf.cell(190, 20, "Grade/Mark-Sheet", align="C")
    pdf.ln()

    with open("std.csv", encoding="utf8") as csv_file:
         data = list(csv.reader(csv_file, delimiter=","))


    pdf.set_font("helvetica", size=14)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_line_width(0.3)
    with pdf.table(
        cell_fill_color=(224, 235, 255),
        col_widths=(42, 39, 35, 42),
        line_height=10,
        text_align=("CENTER"),
        width=190,
    ) as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(datum)


if __name__ == "__main__":
    main()