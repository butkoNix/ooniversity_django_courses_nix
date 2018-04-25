from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from students.models import Student
from students.forms import ModelStudentForm


def list_view(request):
    if 'course_id' in request.GET:
        students = Student.objects.filter(courses=request.GET['course_id'])
    else:
        students = Student.objects.all()
    return render(request, 'students/list.html', {'list_view': students})


def student_detail(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'students/detail.html', {'student': student})


def student_add(request):
    if request.method == 'POST':
        model_form = ModelStudentForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Студент добавлен!')

            return redirect('/students/')
        else:
            messages.error(request, 'ну сука заполни же ты поля!')
    else:
        model_form = ModelStudentForm()
    return render(request, 'students/add.html', {'model_form': model_form})
