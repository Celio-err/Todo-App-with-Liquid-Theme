from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
from app.models import Todo

# Create your views here.
def home(request):
    if request.method == 'POST':
        # Handle form submission to create a new task
        titulu = request.POST.get('titulu')
        deskrisaun = request.POST.get('deskrisaun')
        kategoria = request.POST.get('kategoria')
        prioridade = request.POST.get('prioridade')

        if titulu: # Validasi sederhana agar tidak simpan data kosong
            Todo.objects.create(
                titulu=titulu, 
                deskrisaun=deskrisaun, 
                kategoria=kategoria, 
                prioridade=prioridade
            )
        return redirect('home')

    todos = Todo.objects.all()  
    return render(request, 'home.html', {'todos': Todo.objects.all()})

def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed

    if todo.is_completed:
        todo.completed_at = timezone.now()
    else:
        todo.completed_at = None

    todo.save()
    return redirect('home')

def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('home')