from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from .models import Lesson, Exercise, ExerciseSet, StudentScore
from classes.models import Class


# Displays list of lessons to pick from
class AllLessons(ListView):
    model = Lesson
    template_name = "lessons/all_lessons.html"


# Pull up page with individual Lesson on it. Not questions
class LessonDetail(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'


# Displays questions
def view_lesson_exercises(request, pk):
    lesson = Lesson.objects.get(pk=pk)
    exercises = Exercise.objects.filter(lesson=lesson)
    context = {'lesson': lesson, 'exercises': exercises}
    return render(request, 'lessons/exercises.html', context)


def grade_exercises(request, pk):
    if request.method == 'POST':
        lesson = Lesson.objects.get(pk=pk)
        exercises = Exercise.objects.filter(lesson=lesson)
        total_score = 0

        for exercise in exercises:
            answer_key = str(exercise.correct_answer)
            user_answer = request.POST.get(f'exercise_{exercise.id}')

            if user_answer == answer_key:
                total_score += 1

        percentage_score = (total_score / len(exercises)) * 100

        student_score = StudentScore.objects.create(
            student=request.user, exercise_set=lesson.exerciseset_set.first(), score=percentage_score
        )
        student_score.save()

        return redirect('progress_page')

    return redirect('lessons/lesson_detail', lesson_id=pk)


def progress_page(request):
    user = request.user
    exercise_sets = ExerciseSet.objects.filter(lesson__exerciseset__studentscore__student=user).distinct()

    exercise_set_scores = {}

    for exercise_set in exercise_sets:
        scores = StudentScore.objects.filter(exercise_set=exercise_set, student=user)
        exercise_set_scores[exercise_set] = scores

    context = {'exercise_set_scores': exercise_set_scores}
    return render(request, 'lessons/progress_page.html', context)


def teacher_progress(request):
    # find everything that fits criteria
    teacher_classes = Class.objects.filter(teacher=request.user)
    lessons = Lesson.objects.filter(lesson_class__in=teacher_classes)
    class_students = User.objects.filter(classes__in=teacher_classes).distinct()

    lesson_scores = []
    # go through the lessons
    for lesson in lessons:
        exercise_set = ExerciseSet.objects.filter(lesson=lesson).first()
        # create object
        scores = StudentScore.objects.filter(
            student__in=class_students,
            exercise_set=exercise_set,
        ).order_by('student')
        #  add them to list to display
        lesson_scores.append({
            'lesson': lesson,
            'student_scores': scores,
        })

    context = {'lesson_scores': lesson_scores}
    return render(request, 'lessons/teacher_progress.html', context)
