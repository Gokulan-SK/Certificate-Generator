from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.http import HttpResponse
import os
import io
import uuid 
from ExcelDataIntegration.models  import IncompleteGeneration

def edit(request):
    # Construct the absolute path to the image
    img_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'image', 'certificate_template.jpeg')

    # Open the image
    img = Image.open(img_path)
     
    # Initialize ImageDraw and ImageFont
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf",36) # You might want to use a custom font

    # Add text to the image
    name = IncompleteGeneration.name
    course = IncompleteGeneration.course
    Duration = IncompleteGeneration.duration
    uid=uuid.uuid1()
    name_position = (488, 239) 
    course_position = (536,383) 
    Duration_position = (748,471) 
    uid_position=(100,200) # Adjust the position as needed
    color =(0,0,0)
    draw.text(name_position,text=name,font=font,fill=color)
    draw.text(course_position,text=course,font=font,fill=color)
    draw.text(Duration_position,text=Duration,font=font,fill=color)
    draw.text(uid_position,text=uid,font=font,fill=color)
    img = img.save(f"static/certificates/{name}_img.png")

    # Return the modified image as a response
   
    return render(request,'certificate-template.html',{'name':name})
