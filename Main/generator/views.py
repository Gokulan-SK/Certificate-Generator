from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.http import HttpResponse
import os
import io
import uuid 
from ExcelDataIntegration.models  import IncompleteGeneration
from list.models import CompletedGeneration
from django.contrib.auth.decorators import login_required



@login_required
def edit(request,id):
    # Construct the absolute path to the image
    img_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'image', 'certificate.jpg')

    # Open the image
    img = Image.open(img_path)
     
    # Initialize ImageDraw and ImageFont
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf",36) # You might want to use a custom font

    #retrive the record using the id argument sent from the template
    record=IncompleteGeneration.objects.get(id=id)
    name = record.name
    course = record.course
    Duration = record.duration
    email=record.email
    uid=uuid.uuid1()

    # Add text to the image
    name_position = (792, 385) 
    course_position = (820,629) 
    Duration_position = (962,803) 
    uid_position=(309,1329) # Adjust the position as needed
    color =(0,0,0)
    draw.text(name_position,text=name,font=font,fill=color)
    draw.text(course_position,text=course,font=font,fill=color)
    draw.text(Duration_position,text=Duration,font=font,fill=color)
    draw.text(uid_position,text=str(uid),font=font,fill=color)
    img.save(f"static/certificates/{name}_img.png")


    #saving the record in db
    completed=CompletedGeneration(uid=str(uid),name=name,course=course,duration=Duration,email=email)

    completed.save()

    #removing the record from IncompleteGeneration table
    record.delete()

    # Return the modified image as a response
    return render(request,'certificate-template.html',{'name':name})