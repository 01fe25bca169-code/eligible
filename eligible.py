import sys

total_working_days = int(sys.argv[1])
number_of_attendance = int(sys.argv[2])

attendance_percentage = number_of_attendance / total_working_days * 100

if attendance_percentage > 85:
    print("Student eligible to exam")
else:
    print("Student not eligible to exam")
