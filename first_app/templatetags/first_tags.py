from django import template
from django.template.loader import get_template
register = template.Library()


def my_template(value, arg):
    if arg == 'change':
        value = 'Rahim'
        return value

def show_courses():
    courses =  [
        {
            "id": 1,
            "course": "c",
            "teacher": "NAHID"
        },
        {
            "id": 2,
            "course": "c++",
            "teacher": "HASAN"
        },
        {
            "id": 3,
            "course": "PYTHON",
            "teacher": "MISHUK"
        },
        {
            "id": 4,
            "course": "JAVA",
            "teacher": "NIMAT"
        }
        ]
    return {'courses': courses}
courses_template = get_template('first_app/courses.html')
register.filter("change_name", my_template)
register.inclusion_tag(courses_template)(show_courses)
