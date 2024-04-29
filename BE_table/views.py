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
    record.delete()
    if request.method == 'POST':
        form = FollowupBEForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('BE_table:repport')
    else:
        form = FollowupBEForm(instance=record)
    return render(request, 'BE_table/edit.html', {'form': form, 'record_key': record_id, 'record': record})

"""
@login_required
def export_to_excel(request):
    table_name = 'BE_table_followupbe'
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()

    try:
        # Fetch data from database
        query = cursor.execute(f'SELECT * FROM {table_name}')
        data = cursor.fetchall()  # Fetch results as list of tuples

        # Create workbook and worksheet
        wb = Workbook()
        ws = wb.active
        ws.title = table_name  # Set worksheet title (optional)

        # Write column headers
        headers = [col[0] for col in cursor.description]  # Extract column names
        ws.append(headers)

        # Write data rows
        for row in data:
            ws.append(row)

        # Get user's Downloads folder path
        downloads_folder = os.path.join(os.path.expanduser('~'))


        # Create a filename with timestamp
        filename = f"{table_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"

        # Save the workbook to Downloads folder
        #wb.save(os.path.join(downloads_folder, filename))
        with open(os.path.join(downloads_folder, filename), "wb") as f:
            f.write(filename.encode('utf-8'))

        download_file(request)

        messages.success(request, "Data exported successfully to Excel!")
        return redirect('BE_table:homepage')

    except Exception as e:
        messages.error(request, f"Error exporting data to Excel: {e}")
        return render(request, 'BE_table/home.html')

    finally:
        connection.close()


def download_file(request):
    file_path = f'https://www.pythonanywhere.com/user/JesusGPtto/files/home/JesusGPtto/{filename}'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename=f"{filename}"'
    return response

"""
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
@login_required
def export_to_excel(request):
    import pandas as pd
    table_name = 'BE_table_followupbe'
    connection = sqlite3.connect("db.sqlite3")
    data_frame = pd.read_sql(f'SELECT * FROM {table_name}', connection)

    try:
        # Encode the DataFrame and assign it to a new variable
        excel_file = io.BytesIO()
        writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
        data_frame.to_excel(writer, index=False, sheet_name='be_records')

        # Create a downloadable Excel response
        response = HttpResponse(excel_file.getvalue(), content_type='Spreadsheet files')
        response['Content-Disposition'] = f'attachment; filename={table_name}_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.xlsx'

        # Success message can be displayed on the template
        messages.success(request, "Data exported successfully!")
        writer.save()  # Closing the ExcelWriter object
        excel_file.seek(0)  # Resetting the BytesIO object's cursor to the beginning
        return response

    except Exception as e:
        messages.error(request, f"Error exporting data to excel: {e}")
        return render(request, 'BE_table/home.html')

    finally:
        connection.close()
"""