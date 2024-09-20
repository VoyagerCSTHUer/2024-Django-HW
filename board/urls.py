from django.urls import path, include
import board.views as views

urlpatterns = [
    path('startup', views.startup),
    path('login', views.login),
    path('boards', views.boards),
    # TODO Start: [Student] add routing paths for `boards/<index>` and `user/<userName>`
    path('boards/<index>', views.board),
    path('user/<userName>', views.user),
    # TODO End: [Student] add routing paths for `boards/<index>` and `user/<userName>`

]
