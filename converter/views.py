from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
import pytesseract
from PIL import Image
from pytesseract import pytesseract, image_to_boxes, image_to_data, Output

# Set tesseract path
pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


def image_to_text(request):
    extracted_texts = []

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for uploaded_image in request.FILES.getlist('images'):
                image = Image.open(uploaded_image)
                text = pytesseract.image_to_string(image)
                extracted_texts.append(text)
    else:
        form = ImageUploadForm()

    context = {
        'form': form,
        'extracted_texts': extracted_texts
    }
    return render(request, 'converter/upload_and_convert.html', context)


def image_to_boxes(request):
    boxes = ""
    if request.method == 'POST' and request.FILES['image']:
        image = Image.open(request.FILES['image'])
        boxes = pytesseract.image_to_boxes(image)
    
    context = {
        'boxes': boxes,
    }
    return render(request, 'converter/image_boxes.html', context)


def image_to_data(request):
    data = ""
    if request.method == 'POST' and request.FILES['image']:
        image = Image.open(request.FILES['image'])
        data = pytesseract.image_to_data(image, output_type=Output.STRING)
    
    context = {
        'data': data,
    }
    return render(request, 'converter/image_data.html', context)
