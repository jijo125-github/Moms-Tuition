from django.urls import path
from Student import views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('homepage/',views.homepage_view, name='homenew'),
    path('addStudent/',views.StudentCreate.as_view(), name = 'addStudent'),
    path('editStudent/<int:pk>/',views.StudentUpdate.as_view(), name = 'updateStudent'),
    path('addAddress/',views.AddressCreate.as_view(), name = 'addAddress'),
    path('editAddress/<int:pk>/',views.AddressUpdate.as_view(), name = 'updateAddress'),
    path('addContact/',views.ContactCreate.as_view(), name = 'addContact'),
    path('editContact/<int:pk>/',views.ContactUpdate.as_view(), name = 'updateContact'),
    path('studentDetail/<int:id>/',views.studentDetail, name = 'studentDetail'),
    path('deleteStudent/<int:pk>/',views.StudentDelete.as_view(), name = 'deleteStudent'),
    path('addStudentCard/',views.addStudentCard, name = 'StudentCard'),
    # path('postStudent/',views.post_student_view),
    # path('addStudentForm/',views.add_studentform_view),
    # path('getaddress/<int:id>/',views.get_address, name = 'addr'),
    # path('studentMiniInfo/',views.student_list_view),
    # path('testingpurpose/<int:pk>/',views.get_addressid),
    # handler404 = 'my_app.views.page_not_found'
    path('StudentsInfo/',views.StudentsMini.as_view()),
    path('GetStudentDetail/<int:id>/',views.GetStudentDetail.as_view()),
    path('GetStudentFilterInfo/', views.StudentListViewFilter.as_view(), name = 'filterStudent'),
    path('GetStudentSortByName/', views.filterStudentByName, name = 'SortbyName'),
    path('GetStudentSortByAge/', views.filterStudentByAge, name = 'SortbyAge')
]