from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    form = QuadraticForm()
    discriminant = result_text = {}
    if request.GET:
        form = QuadraticForm(request.GET)

        if (form.is_valid()):
            arguments = get_form_arguments(form)
            discriminant = get_discriminant(arguments)
            result_text = get_result_text(discriminant, arguments)

    return render(request, "quadratic/results.html", {
        'form': form,
        'discriminant': discriminant,
        'result_text': result_text
    })


def get_discriminant(arguments):
    return int(arguments['b']) ** 2 - 4 * int(arguments['a']) * int(arguments['c'])


def get_form_arguments(form):
    arguments = {}
    for element in form.data:
        arguments[element] = int(form.data[element])

    return arguments


def get_result_text(discriminant, arguments):
    if discriminant == 0:
        x = calc_root(discriminant, arguments)
        return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
    elif discriminant < 0:
        return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        x1 = calc_root(discriminant, arguments)
        x2 = calc_root(discriminant, arguments, 2)
        return 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)


def calc_root(discriminant, arguments, order=1):
    if order == 1:
        x = (-arguments['b'] + discriminant ** (1 / 2.0)) / 2 * arguments['a']
    else:
        x = (-arguments['b'] - discriminant ** (1 / 2.0)) / 2 * arguments['a']
    return x
