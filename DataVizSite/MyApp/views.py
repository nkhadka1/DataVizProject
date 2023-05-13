import os
from collections import Counter

import pandas as pd

from django.shortcuts import render, redirect, reverse
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Data
from .forms import DataForm


# Create your views here.

#Index
def index(request):
    context = {}
    return render(request, "MyApp/index.html", context)

#FOR UPLOADING THE FILE
def uploadfile_home(request):
    context = {}
    global attribute

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #print(uploaded_file)
        attribute = request.POST.get('attributeid')

        # check if the file is a csv file or not. If yes, save in media folder
        if uploaded_file.name.endswith('.csv'):
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file)
            #Everytime you upload file, it is saved in a different name
            dir = os.getcwd()
            file_directory = dir+'\media\\'+name
            readfile(file_directory)

            request.session['attribute'] = attribute

            if attribute not in data.axes[1]:
                messages.warning(request, 'Please write the column name correctly.')
            else:
                print(attribute)
                return redirect(filepie)

            return redirect(filepie)

        else:
            messages.warning(request, 'The file extension did not match. Please use csv files.')

    return render(request, "MyApp/uploadfile_home.html", context)


def readfile(filename):
    global rows,columns,data,my_file,missingvalues

    # read the missing data - checking if there is a null
    missingvalues = ['?', '0', '--']

    my_file = pd.read_csv(filename, sep='[,:;|_]', na_values=missingvalues, engine='python')
    data = pd.DataFrame(data=my_file, index=None)

    rows = len(data.axes[0])
    columns = len(data.axes[1])
    null_data = data[data.isnull().any(axis=1)]
    missingvalues = len(null_data)


#FOR ENTERING DATA
def databar(request):
    data = Data.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data-bar')
    else:
        form = DataForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'MyApp/data-bar.html', context)

def dataline(request):
    data = Data.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data-line')
    else:
        form = DataForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'MyApp/data-line.html', context)

def datapie(request):
    data = Data.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data-pie')
    else:
        form = DataForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'MyApp/data-pie.html', context)

def dataradar(request):
    data = Data.objects.all()
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data-radar')
    else:
        form = DataForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'MyApp/data-radar.html', context)

#--------------------------------------------------------------------------------------------------
#FILE GRAPH VIEWS

#PIE CHART
def filepie(request):

    message = 'The file has been successfully uploaded. There are ' + str(rows) + ' rows and ' + str(columns) + ' columns.'
    messages.warning(request, message)

    dashboard = []
    for d in data[attribute]:
        dashboard.append(d)

    my_dashboard = dict(Counter(dashboard))

    keys = my_dashboard.keys()
    values = my_dashboard.values()

    listkeys=[]
    listvalues=[]

    for k in keys:
        listkeys.append(k)

    for v in values:
        listvalues.append(v)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return render(request, 'MyApp/file-pie.html', context)


#BAR GRAPH
def filebar(request):
    message = 'The file has been successfully uploaded. There are ' + str(rows) + ' rows and ' + str(
        columns) + ' columns.'
    messages.warning(request, message)

    dashboard = []
    for d in data[attribute]:
        dashboard.append(d)

    my_dashboard = dict(Counter(dashboard))

    keys = my_dashboard.keys()
    values = my_dashboard.values()

    listkeys = []
    listvalues = []

    for k in keys:
        listkeys.append(k)

    for v in values:
        listvalues.append(v)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return render(request, "MyApp/file-bar.html", context)

#LINE GRAPH
def fileline(request):
    message = 'The file has been successfully uploaded. There are ' + str(rows) + ' rows and ' + str(
        columns) + ' columns.'
    messages.warning(request, message)

    dashboard = []
    for d in data[attribute]:
        dashboard.append(d)

    my_dashboard = dict(Counter(dashboard))

    keys = my_dashboard.keys()
    values = my_dashboard.values()

    listkeys = []
    listvalues = []

    for k in keys:
        listkeys.append(k)

    for v in values:
        listvalues.append(v)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return render(request, "MyApp/file-line.html", context)

#FILE RADAR
def fileradar(request):
    message = 'The file has been successfully uploaded. There are ' + str(rows) + ' rows and ' + str(
        columns) + ' columns.'
    messages.warning(request, message)

    dashboard = []
    for d in data[attribute]:
        dashboard.append(d)

    my_dashboard = dict(Counter(dashboard))

    keys = my_dashboard.keys()
    values = my_dashboard.values()

    listkeys = []
    listvalues = []

    for k in keys:
        listkeys.append(k)

    for v in values:
        listvalues.append(v)

    context = {
        'listkeys': listkeys,
        'listvalues': listvalues,
    }

    return render(request, "MyApp/file-radar.html", context)
