from django.urls import path
from main.views import show_main, create_camera_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, create_tokocamera_form_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_camera
from main.views import delete_camera





app_name = 'main'

urlpatterns = [
    # Main Page
    path('', show_main, name='show_main'),
    path('api/xml/', show_xml, name='show_xml'),
    path('api/json/', show_json, name='show_json'),
    path('api/xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('api/json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-camera/<uuid:id>/', edit_camera, name='edit_camera'),
    path('create-camera-entry/', create_camera_entry, name='create_camera_entry'),
    path('delete-camera/<uuid:id>/', delete_camera, name='delete_camera'),
    path('create-camera-ajax/', create_tokocamera_form_ajax, name='create_camera_ajax'),
]
