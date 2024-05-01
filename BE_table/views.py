from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import FollowupBE
from .forms import FollowupBEForm
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
import sqlite3
from datetime import datetime
from django.http import HttpResponse

def homepage(request):
    today = date.today()
    day_name = today.strftime("%A") + " " + str(today)
    return render(request, 'BE_table/header.html', {'day': day_name})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("BE_table:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="BE_table/login.html", context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('BE_table:homepage')

def insert(request):
    form = FollowupBEForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('BE_table:report')
    # else:
    #     form = FollowupBE()
    return render(request, 'BE_table/insert.html', {'form': form})


def report(request):
    # Get all gym joiners and their additional details
    records = FollowupBE.objects.all()
    # select_related is to perform a SQL join between two tables in a single query
    return render(request, 'BE_table/report.html', {'records': records})

@login_required
def edit(request, record_id):
    record = FollowupBE.objects.get(id=record_id)
    if request.method == 'POST':
        form = FollowupBEForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('BE_table:report')
    else:
        form = FollowupBEForm(instance=record)
    return render(request, 'BE_table/edit.html', {'form': form, 'record_key': record_id, 'record': record})

@login_required
def export_to_excel(request):
    import pandas as pd
    table_name = 'BE_table_followupbe'
    connection = sqlite3.connect("db.sqlite3")
    data_frame = pd.read_sql(f'SELECT * FROM {table_name}', connection)

    try:
        # Generate data as CSV
        csv_data = data_frame.to_csv(index=False)

        # Create a downloadable CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={table_name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
        response.write(csv_data.encode('utf-8'))

        # Success message can be displayed on the template
        messages.success(request, "Data exported successfully! You can download the CSV file.")
        return response

    except Exception as e:
        messages.error(request, f"Error exporting data to CSV: {e}")
        return render(request, 'BE_table/home.html')

    finally:
        connection.close()

"""
def edit(request, record_id):
    record = FollowupBE.objects.get(id=record_id)
    
    record.advance = 666
    record.save()
        # form = FollowupBEForm(request.POST, instance=record)
        #if form.is_valid():
            #form.save()
    #return redirect('BE_table:report')
    # else:
    #     form = FollowupBEForm(instance=record)
    return render(request, 'BE_table/edit.html', {'record_key': record_id, 'record': record})

"""
"""
@login_required
def edit(request, record_id):
    record = FollowupBE.objects.get(id=record_id)
    form = FollowupBEForm(request.POST, instance=record)
    if form.is_valid():
        form = FollowupBEForm(request.POST, instance=record)
        form.save()
        return redirect('BE_table:report')
    else:
        form = FollowupBEForm(instance=record)
    return render(request, 'BE_table/edit.html', {'form': form, 'record_key': record_id, 'record': record})
"""

