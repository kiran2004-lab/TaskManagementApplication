from django.shortcuts import render, redirect
from .models import TaskDetails

def taskpost(request):
    return render(request, 'teamleadmodule/taskpost.html')

def add_task_details(request):
    if request.method == 'POST':
        Task_Title = request.POST.get('TaskTitle')
        Task_Priority = request.POST.get('TaskPriority')
        Start_Date = request.POST.get('StartDate')
        End_Date = request.POST.get('EndDate')
        Description = request.POST.get('Description')
        Task_Details = TaskDetails(
            Task_Title=Task_Title,
            Task_Priority=Task_Priority,
            Start_Date=Start_Date,
            End_Date=End_Date,
            Description=Description,
        )
        Task_Details.save()
        return render(request, 'teamleadmodule/datainserted.html')
    return render(request, 'teamleadmodule/teamleadhomepage.html')

def view_task_details(request):
    task_details_list = TaskDetails.objects.all()
    return render(request, 'teamleadmodule/view_task_details.html', {'task_details_list': task_details_list})

