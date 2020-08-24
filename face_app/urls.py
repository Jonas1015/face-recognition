from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name  ='home'),
    # =================== Filter by Courses ====================================
    path('students/<int:id>/course/', byCourses, name  ='by-courses'),
    # ================== STUDENTS ==============================================
    path('all-students/', allStudents, name  ='all-students'),
    path('add-student/', addStudent, name  ='add-student'),
    path('update-student/<int:id>/', updateStudent, name  ='update-student'),
    path('view-student/<int:id>/', viewStudent, name  ='view-student'),
    path('delete-student/<int:id>/', deleteStudent, name  ='delete-student'),


    # ===================== COURSES ============================================
    path('filter-by/courses/', filterCourses, name  ='filter-courses'),
    path('all-courses/', allCourses, name  ='all-courses'),
    path('add-course/', addCourse, name  ='add-course'),
    path('update-course/<int:id>/', updateCourse, name  ='update-course'),
    path('delete-course/<int:id>/', deleteCourse, name  ='delete-course'),

    #===================== RECOGNITION ITSELF ==================================
    path('test-student-image/', detectImage, name  ='test-image'),
    path('test-video/', video, name  = 'video'),
    path('view-result/<int:id>/', viewResult, name  ='view-result'),

]
