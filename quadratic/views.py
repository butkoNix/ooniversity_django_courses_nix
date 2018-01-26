from django.shortcuts import render
from django import forms


class QuadraticForm(forms.Form):

    a = forms.CharField(max_length=10)
    b = forms.CharField(max_length=10)
    c = forms.CharField(max_length=10)


def quadratic_results(request):
    args = collect_args(request)
    context = validate(args)
    form = QuadraticForm()
    context['form'] = form
    if not context['error']:
        context['descr'] = get_descriminant(context)
    if not context['error']:
        context['result_text'] = get_result_text(context)

    return render(request, "quadratic/results.html", context)


def collect_args(request):
    args = dict()
    args['a'] = (request.GET['a'])
    args['b'] = (request.GET['b'])
    args['c'] = (request.GET['c'])

    return args


def get_descriminant(arguments):
    return arguments['b']['val'] ** 2 - 4 * arguments['a']['val'] * arguments['c']['val']


def get_result_text(arguments):
    if arguments['descr'] == 0:
        x = calc_root(arguments)
        return 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = ' + str(x)
    elif arguments['descr'] < 0:
        return 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
    else:
        x1 = calc_root(arguments)
        x2 = calc_root(arguments, 2)
        return 'Квадратное уравнение имеет два действительных корня: x1 = ' + str(x1) + ', x2 = ' + str(x2)


def calc_root(arguments, order=1):
    if order == 1:
        x = (-arguments['b']['val'] + arguments['descr'] ** (1 / 2.0)) / 2 * arguments['a']['val']
    else:
        x = (-arguments['b']['val'] - arguments['descr'] ** (1 / 2.0)) / 2 * arguments['a']['val']
    return x


def validate(args):
    error = False
    resp = {}
    for key in args:
        err_message = ''
        val = args[key]
        if not val:
            err_message = 'коэффициент не определен'
            error = True
        else:
            try:
                val = int(val)
                if key == 'a' and val == 0:
                    err_message = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
                    error = True
            except ValueError:
                err_message = 'коэффициент не целое число'
                error = True

        resp[key] = {'val': val, 'err_message': err_message}
    resp['error'] = error

    return resp
