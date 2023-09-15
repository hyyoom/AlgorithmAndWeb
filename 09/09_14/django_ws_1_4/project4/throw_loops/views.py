from django.shortcuts import render

# Create your views here.
def first(r):
    data= r.GET.get('message1')
    context={
        'data':data
    }
    return render(r, 'throw_loops/first.html',context)


def second(r):
    data1 = r.GET.get('message1')
    context={
        'data1' : data1,
    }
    return render(r, 'throw_loops/second.html', context)


def third(r):
    data1 = r.GET.get('message1')
    data2 = r.GET.get('message2')
    context={
        'data': [data1, data2]
    }
    return render(r, 'throw_loops/third.html', context)