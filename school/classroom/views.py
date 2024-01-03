from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from .models import Teacher
from classroom.forms import ContactForm

# Create your views here.
# def home_view (request):
#     return render(request,"classroom/home.html")

class HomeView(TemplateView):
    template_name = "classroom/home.html"

class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"

    # success_url = "/classroom/thank_you/"
    success_url = reverse_lazy("classroom:thank_you")

    def form_valid(self, form):
        #with the cleaned data
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherCreateView(CreateView):
    model = Teacher
    #model_form.html
    fields = "__all__"
    success_url = reverse_lazy("classroom:thank_you")

class TeacherListView(ListView):
    model = Teacher
    context_object_name = "teacher_list"
    queryset = Teacher.objects.order_by('first_name')

class TeacherDetailView(DetailView):
    model = Teacher

class TeacherUpdateView(UpdateView):
    model = Teacher
    #fields =['last_name','first_name']
    fields = "__all__"
    success_url = reverse_lazy("classroom:list_teacher")
class TeacherDeleteView (DeleteView):
    model = Teacher
    success_url = reverse_lazy("classroom:list_teacher")