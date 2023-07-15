from django.shortcuts import render,redirect,get_object_or_404
from .models import Notes
from .form import NewNote


def home(request):
    data = Notes.objects.all()
    context = { 'notes': data}
    return render(request, template_name='notes/home.html', context=context)

def new_note(request):
    if request.method == 'POST':
        form = NewNote(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('home')
    else:    
        form = NewNote()
    return render(request,template_name="notes/note_form.html",context={"form":form})
    

def edit_note(request, id):
    note = get_object_or_404(Notes, id=id)
    if request.method == "POST":
        form = NewNote(request.POST, instance=note)
        if form.is_valid():
            note.save()
            return redirect('home')
    else:
        form = NewNote(instance=note)
    return render(request, 'notes/edit_form.html', {'form': form})

def status_change(request,id):
    note = get_object_or_404(Notes, id=id)
    note.is_completed = not note.is_completed
    note.save()
    return redirect('home')
    
def delete(request, id):
    Notes.objects.get(id=id).delete()
    return redirect('home')
