from django.http import Http404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NotesForm
from .models import Notes

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False) # cria o objeto, mas nao salva na database
        self.object.user = self.request.user # add a user
        self.object.save() # save the note with the user in the database
        return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'notes/notes_list.html'
    login_url = 'admin' # vai para a pagina admin

    def get_queryset(self):
        return self.request.user.notes.all()#pegar tudo só daquele usuario


class NotesDetailView(DetailView):
    model = Notes
    context_object_name ='note'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes':all_notes})


# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.html', {'note': note})