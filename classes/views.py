from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Class
import uuid
from .forms import ClassCreationForm, ClassForm, JoinClass
from accounts.models import Profile
from lessons.models import Lesson


def is_teacher(user):
    return user.profile.is_teacher


@user_passes_test(is_teacher, login_url='home')
def create_class(request):
    if request.method == 'POST':
        form = ClassCreationForm(request.POST)
        if form.is_valid():
            class_name = form.cleaned_data['class_name']
            teacher = request.user
            # Generates code
            class_code = uuid.uuid4()
            # Creates class
            new_class = Class(name=class_name, teacher=teacher, class_code=class_code)
            new_class.save()
            # Updates teachers profile
            teacher_profile = Profile.objects.get(user=teacher)
            teacher_profile.class_field = new_class
            teacher_profile.save()
            # Associates 3 pre-made lessons with every class
            # I have them associated because I want teachers to be able to create their own in the future
            pre_made_lessons = Lesson.objects.filter(title__in=["Quadratic Equations and Their Solutions",
                                                                "Exploring Symbolism in Literature",
                                                                "Photosynthesis: Nature's Energy Conversion Process"])
            new_class.lessons.set(pre_made_lessons)

            return redirect('class_detail', class_id=new_class.id)
    else:
        form = ClassCreationForm()

    return render(request, 'classes/create_class.html', {'form': form})


def class_detail(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)

    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClassForm(instance=class_obj)

    return render(request, 'classes/class_detail.html', {'class_obj': class_obj, 'form': form})


def join_class(request):
    if request.method == 'POST':
        form = JoinClass(request.POST)

        if form.is_valid():
            class_code = form.cleaned_data['class_code']

            # Enter code wrong or right
            try:
                class_obj = Class.objects.get(class_code=class_code)
            except Class.DoesNotExist:
                form.add_error('class_code', 'Class not found. Please check the code.')
                return render(request, 'classes/join_class.html', {'form': form})

            # If student not in class, add them
            if request.user not in class_obj.students.all():
                class_obj.students.add(request.user)

                # Set the class_field to the class they are joining
                student_profile, created = Profile.objects.get_or_create(user=request.user)
                student_profile.class_field = class_obj
                student_profile.save()

                return redirect('home')
            else:
                return redirect('join_class')

    else:
        form = JoinClass()

    return render(request, 'classes/join_class.html', {'form': form})
