from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

# List students
def student_list(request):
    query = request.GET.get('q')
    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students = Student.objects.all()
    return render(request, "students/student_list.html", {"students": students})

# Add student
def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "students/student_form.html", {"form": form})

# Update student
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "students/student_form.html", {"form": form})

# Delete student
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "students/student_confirm_delete.html", {"student": student})