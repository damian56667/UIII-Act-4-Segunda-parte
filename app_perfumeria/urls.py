from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_perfumeria, name='inicio_perfumeria'),

    # Empleado
    path('empleado/', views.ver_empleado, name='ver_empleado'),
    path('empleado/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleado/actualizar/<int:empleado_id>/', views.actualizar_empleado, name='actualizar_empleado'),
    path('empleado/actualizar/realizar/<int:empleado_id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleado/borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),

    # Producto
    path('producto/', views.ver_producto, name='ver_producto'),
    path('producto/agregar/', views.agregar_producto, name='agregar_producto'),
    path('producto/actualizar/<int:producto_id>/', views.actualizar_producto, name='actualizar_producto'),
    path('producto/actualizar/realizar/<int:producto_id>/', views.realizar_actualizacion_producto, name='realizar_actualizacion_producto'),
    path('producto/borrar/<int:producto_id>/', views.borrar_producto, name='borrar_producto'),
]
