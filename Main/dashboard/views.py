from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from list.models import CompletedGeneration
from datetime import datetime, timedelta
from django.db.models import Count

# Create your views here.

@login_required
def dashboard(request):
    

    total_generations = CompletedGeneration.objects.aggregate(total=Count('id'))['total']
    
    today = datetime.now().date()
    todays_generations = CompletedGeneration.objects.filter(generation_time__date=today).count()

    
    this_week_start = today - timedelta(days=today.weekday())
    this_weeks_generations = CompletedGeneration.objects.filter(generation_time__date__gte=this_week_start).count()
    
    most_popular_course = CompletedGeneration.objects.values('course').annotate(count=Count('id')).order_by('-count', 'course').first()
    most_popular_course_name = most_popular_course['course'] if most_popular_course else None
    most_popular_course_count = most_popular_course['count'] if most_popular_course else 0


    
    context = {
        'total_generations': total_generations,
        'todays_generations': todays_generations,
        'this_weeks_generations': this_weeks_generations,
        'most_popular_course_name': most_popular_course_name,
        'most_popular_course_count' : most_popular_course_count,
        
    }


    return render(request,'dashboard.html',context)

@login_required
def generate_list(request):
    return render(request, 'generate-list.html',{})

@login_required
def certificate_template(request):
    return render(request, 'certificate-template.html', {})


