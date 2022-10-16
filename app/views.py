from django.shortcuts import render
from django.core.files import File
from app.models import Document


def Document_save(request):
    if request.method=="POST":
        audio = request.FILES["audio"]
        audio_file = Document.objects.create(name=audio.name,file=audio)
        audio_path = audio_file.file.path
        return render(request, "index.html", {"audio_path":audio_path})
    return render(request, "index.html")