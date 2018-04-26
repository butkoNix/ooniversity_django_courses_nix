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
        model_form = ModelStudentForm()
    return render(request, 'students/add.html', {'model_form': model_form})


def student_remove(request, pk):
    try:
        student = Student.objects.get(id=pk)
        if request.method == 'POST':
            student.delete()
            messages.success(request, 'Студент %s %s успешно удален!' % (student.name, student.surname))
            return redirect('/students/')
    except Student.DoesNotExist:
        return redirect('/students/')

    return render(request, 'students/remove.html', {'student': student})


def student_edit(request, pk):
    try:
        student = Student.objects.get(id=pk)
        if request.method == 'POST':
            form = ModelStudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                messages.success(request, 'Данные изменены.')
                return redirect('/students/')
        else:
            form = ModelStudentForm(instance=student)
    except Student.DoesNotExist:
        return redirect('/students/')

    return render(request, 'students/edit.html', {'student': student, 'form': form})
