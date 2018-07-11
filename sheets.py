from collections import namedtuple
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open("gradebook").sheet1


Grade = namedtuple('Grade', ['student_id', 'exercise_id', 'result'])
Grid = namedtuple('Grid', ['exercises_axis', 'students_axis'])


def record_grade(grid, grade):
    # TODO: error handling
    # HACK: Sheets indexes from 1 ... this will cause bugs
    row = grid.students_axis.index(grade.student_id) + 1
    col = grid.exercises_axis.index(grade.exercise_id) + 1
    wks.update_cell(row, col, grade.result)

def grid():
    # A hack. wks.find('query') was causing some weird error ...
    exercises = wks.row_values(1)
    students = wks.col_values(1)
    return Grid(exercises_axis=exercises, students_axis=students)


if __name__ == '__main__':
    grade = Grade('justin-moen', 'lesson-2', 'pass')
    record_grade(grid(), grade)
