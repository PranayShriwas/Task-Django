from django.shortcuts import render, redirect
from .forms import UserInputForm
from .models import UserInput

def user_input_view(request):
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('input_success')
    else:
        form = UserInputForm()
    
    return render(request, 'user_input_form.html', {'form': form})

def input_success(request):
    user_inputs = UserInput.objects.all()
    return render(request, 'input_success.html', {'user_inputs': user_inputs})
