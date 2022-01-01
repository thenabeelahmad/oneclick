from django.shortcuts import render

# Create your views here.

from django.http import FileResponse
import os
 
def show_pdf(request):
    if request.method=='POST':
        id = request.POST['txtRollNo']
        rid = f'{id}.pdf'
    try:
        filepath = os.path.join('media',rid)
        return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
    except:
        return render(request,'oneclick.html',{'msg':'No Pdf for this Roll No'})

def index(request):
    return render(request,'oneclick.html')

