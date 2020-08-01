from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import F, Q
from .forms import *
import face_recognition
from PIL import Image, ImageDraw
import numpy as np

# Create your views here.
def home(request):
    students_number = Student.objects.all().count()
    courses_number = Course.objects.all().count()

    context = {
        'students_number': students_number,
        'courses_number': courses_number,
    }
    mytemplate = 'face/home.html'
    return render(request, mytemplate, context)


# ============================== STUDENTS =====================================
def allStudents(request):
    get_students = Student.objects.all()
    query = request.GET.get("q")
    if query:
        if get_students.filter(Q(fname__icontains = query)| Q(lname__icontains = query)):
            get_students = get_students.filter(Q(fname__icontains = query)| Q(lname__icontains = query))
        elif get_students.filter(Q(regno__icontains = query)):
            get_students = get_students.filter(Q(regno__icontains = query))

    myTemplate = 'face/allStudents.html'
    context = {
        'students': get_students,
    }
    return render(request, myTemplate, context)

def byCourses(request, id):
    filtered_students = Student.objects.filter(course = id)
    query = request.GET.get("q")
    if query:
        if filtered_students.filter(Q(fname__icontains = query)| Q(lname__icontains = query)):
            filtered_students = filtered_students.filter(Q(fname__icontains = query)| Q(lname__icontains = query))
        elif filtered_students.filter(Q(regno__icontains = query)):
            filtered_students = filtered_students.filter(Q(regno__icontains = query))
    context = {
        'students': filtered_students,
    }
    myTemplate = 'face/byCourses.html'
    return render(request, myTemplate, context)

def addStudent(request):
    form = addStudentForm()
    if request.method == 'POST':
        form = addStudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Verify faces in the image first capture imafe from the form
            posted_image = request.FILES['image']
            # then load it in the face_recognition library
            image = face_recognition.load_image_file(posted_image)
            # Check for faces with face_locations function
            locations = face_recognition.face_locations(image)
            # if there was no face detected
            if len(locations) < 1:
                messages.warning(request, f'No face was detected from the photo, use another one!')
                return redirect('add-student')
            # If more than a single face was detected
            elif len(locations) > 1:
                messages.warning(request, f'There were more than one face detected. Don\'t use this kind of photo')
                return redirect('add-student')
            # If only one face was detected
            else:
                form.save()
                messages.success(request, f'Student added successfully!')
                return redirect('add-student')
    else:
        form = addStudentForm()
        context = {
            'form': form,
        }
        myTemplate = 'face/addStudent.html'
        return render(request, myTemplate, context)

def updateStudent(request, id):
    instance = get_object_or_404(Student, pk = id)
    form = updateStudentForm(request.POST or None,request.FILES or None, instance = instance)
    # if form.is_valid():
    #     if request.FILES('image'):
    #         # Verify faces in the image first capture imafe from the form
    #         posted_image = request.FILES('image')
    #         # then load it in the face_recognition library
    #         image = face_recognition.load_image_file(posted_image)
    #         # Check for faces with face_locations function
    #         locations = face_recognition.face_locations(image)
    #         # if there was no face detected
    #         if len(locations) < 1:
    #             messages.warning(request, f'No face was detected from the photo, use another one!')
    #             return redirect('update-student')
    #         # If more than a single face was detected
    #         elif len(locations) > 1:
    #             messages.warning(request, f'There were more than one face detected. Don\'t use this photo')
    #             return redirect('update-student')
    #         # If only one face was detected
    #         else:
    #             form.save()
    #             messages.success(request, f'Student has been updated successifully!')
    #             return redirect ('view-student')
    #     else:
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, f'Student has been updated successifully!')
    #             return redirect ('view-student')
    if form.is_valid():
        form.save()
        messages.success(request, f'Student has been updated successifully!')
        return redirect ('all-students')
    context = {
        'form': form,
    }
    myTemplate = 'face/updateStudent.html'
    return render(request, myTemplate, context)


def viewResult(request, id):
    student = get_object_or_404(Student, pk = id)
    context = {
        'student': student
    }
    myTemplate = 'face/viewResult.html'
    return render(request, myTemplate, context)


def viewStudent(request, id):
    student = get_object_or_404(Student, pk = id)
    context = {
        'student': student
    }
    myTemplate = 'face/viewStudent.html'
    return render(request, myTemplate, context)

def deleteStudent(request, id):
    get_data = get_object_or_404(Student, pk = id)
    get_data.delete()
    messages.success(request, f'Student deleted successfull!')
    return redirect('all-students')


# =========================== COURSES ==========================================

def filterCourses(request):
    get_courses = Course.objects.all()
    query = request.GET.get("q")
    if query:
        get_courses = get_courses.filter(Q(name__icontains = query) |Q(code__icontains = query) )

    myTemplate = 'face/filterCourses.html'
    context = {
        'courses': get_courses,
    }
    return render(request, myTemplate, context)

def allCourses(request):
    get_courses = Course.objects.all()
    query = request.GET.get("q")
    if query:
        get_courses = get_courses.filter(Q(name__icontains = query) |Q(code__icontains = query) )

    myTemplate = 'face/allCourses.html'
    context = {
        'courses': get_courses,
    }
    return render(request, myTemplate, context)

def addCourse(request):
    form = addCourseForm()
    if request.method == 'POST':
        form = addCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Course added successfully!')
            return redirect('add-course')
    form = addCourseForm()
    context = {
        'form': form,
    }
    myTemplate = 'face/addCourse.html'
    return render(request, myTemplate, context)

def updateCourse(request, id):
    instance = get_object_or_404(Course, pk = id)
    form = updateCourseForm(request.POST or None, request.FILES or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, f'Course has been updated successifully!')
        return redirect ('all-courses')
    context = {
        'form': form,
    }
    myTemplate = 'face/updateCourse.html'
    return render(request, myTemplate, context)


def deleteCourse(request, id):
    get_data = get_object_or_404(Course, pk = id)
    get_data.delete()
    messages.success(request, f'Course deleted successfull!')
    return redirect('all-courses')




# ====================== FACE RECOGNITION LOGICS ======================================
def detectImage(request):
    if request.method == 'POST':
        # Get a file from the template/form
        myfile = request.FILES['image']

        # Loading image of the unknown in face_recognition library
        unknown_image = face_recognition.load_image_file(myfile)
        # Check if faces are available in the picture
        unknown_face_locations = face_recognition.face_locations(unknown_image)

        # Put a condition to execute some code due to number of faces
        if len(unknown_face_locations) == 1:
            # We emcode the unknown face after detecting it
            unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

            # We first load all data from the table
            students = Student.objects.all()


            # Now working with each dataset from the queryset
            for student in students:
                # loading image from the dataset to face_recognition  library
                known_image = face_recognition.load_image_file(student.image)
                # Encoding image
                student_encoding = face_recognition.face_encodings(known_image)[0]

                # Lets compare the faces one after another since we are in the loop
                results = face_recognition.compare_faces([student_encoding], unknown_encoding, 0.5)

                # Check if any result was found
                if results[0]:
                    myTemplate = 'face/results.html'
                    context = {
                        'student': student,
                        'file': myfile,
                    }
                    return render(request, myTemplate, context )
            # If no image was matched return the message
            # messages.warning(request, f'None of the image matched your picture!')
            # return redirect('test-image')
        elif len(unknown_face_locations) > 1:
            # Holding students variable
            students = []
            all_students = Student.objects.all()
            # Since we loaded and took locations already, now encode the test image
            unknown_group_encodings = face_recognition.face_encodings(unknown_image, unknown_face_locations)

            for (top, right, bottom, left), unknown_face_encoding in zip(unknown_face_locations, unknown_group_encodings):
                # Loop through students first
                for student in all_students:
                    # loading image from the dataset to face_recognition  library
                    known_image = face_recognition.load_image_file(student.image)
                    # Encoding student image
                    student_encoding = face_recognition.face_encodings(known_image)[0]

                    # Lets compare the faces one after another since we are in the loop
                    results = face_recognition.compare_faces([student_encoding], unknown_face_encoding, tolerance = 0.40)

                    # Check if any result was found
                    if results[0]:
                        students.append(student)
                        # for face_location in unknown_face_locations:
                        #     top, right, bottom, left = face_location
                        #     face_image = unknown_image[top:bottom, left:right]
                        #     image = Image.fromarray(face_image)
                        #     image.show()
                        print(student.fname)
                        break
            print(students)
            # check if students list is populated, if not return a message
            if len(students) == 1:
                context = {
                    'student': students[0],
                }
                myTemplate = 'face/results.html'
                return render(request, myTemplate, context)

            elif len(students) > 1:
                context = {
                    'students': students,
                }
                myTemplate = 'face/results.html'
                return render(request, myTemplate, context)
            else:
                messages.warning(request, f'There was none of the face matched from your image!!')
                return redirect('test-image')


            # messages.warning(request, f'There were more than one face in your photo, can\'t compare!!')
            # return redirect('test-image')
        else:
            messages.warning(request, f'Sorry!! We Can\'t load this photo since it is either landscape positioned or has poor quality hence no face could be detected!! You can use another photo if any instead!!')
            return redirect('test-image')

        #  Incase face was detected but there were no match from the database
        messages.warning(request, f'No one was resembling to your photo!!')
        return redirect('test-image')


    myTemplate = 'face/testImage.html'
    context = {}
    return render(request, myTemplate, context)
