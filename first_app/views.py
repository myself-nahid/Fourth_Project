from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, './first_app/home.html', {"name": "NAHID HASAN", "marks": 86,
                                                      "courses": [
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
                                                      ]})

def about(request):
    return render(request, './first_app/about.html', {"author": "Gleen Maxweel"})