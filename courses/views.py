from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.contrib import messages
from courses.models import Course, Lesson
from courses.forms import ModelCourseForm


def detail(request, pk):
    course = Course.objects.get(id=pk)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/detail.html', {'course': course, 'lesson_list': lessons})


def list_view(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'list_view': courses})


def course_detail(request, pk):
    try:
        course = Course.objects.get(id=pk)
    except Course.DoesNotExist:
        return HttpResponseNotFound()
    return render(request, 'courses/detail.html', {'course': course})


def course_add(request):
    if request.method == 'POST':
        model_form = ModelCourseForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            messages.success(request, 'Студент добавлен!')

            return redirect('/courses/')
    else:
        model_form = ModelCourseForm()
    return render(request, 'courses/add.html', {'model_form': model_form})


def course_remove(request, pk):
    try:
        course = Course.objects.get(id=pk)
        if request.method == 'POST':
            course.delete()
            messages.success(request, 'Курс %s успешно удален!' % course.name)
            return redirect('/courses/')
    except Course.DoesNotExist:
        return redirect('/courses/')

    return render(request, 'courses/remove.html', {'course': course})


def course_edit(request, pk):
    try:
        course = Course.objects.get(id=pk)
        if request.method == 'POST':
            form = ModelCourseForm(request.POST, instance=course)
            if form.is_valid():
                form.save()
                messages.success(request, 'Данные изменены.')
                return redirect('/courses/')
        else:
            form = ModelCourseForm(instance=course)
    except Course.DoesNotExist:
        return redirect('/courses/')

    return render(request, 'courses/edit.html', {'course': course, 'form': form})
