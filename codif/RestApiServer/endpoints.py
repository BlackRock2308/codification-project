from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from RestApiServer.apiviews import pavillonviews, chambreviews, etudiantviews, paymentviews, codificationviews

urlpatterns = [
    path("api/pavillons", pavillonviews.PavillonList.as_view()),
    path("api/pavillons/<int:pk>", pavillonviews.PavillonDetail.as_view()),

    path("api/chambres", chambreviews.ChambreList.as_view()),
    path("api/chambres/<int:pk>", chambreviews.ChambreDetail.as_view()),

    path("api/etudiants", etudiantviews.EtudiantList.as_view()),
    path("api/etudiants/<int:pk>", etudiantviews.EtudiantDetail.as_view()),

    path("api/payments", paymentviews.PaymentList.as_view()),
    path("api/payments/<int:pk>", paymentviews.PaymentDetail.as_view()),

    path("api/codifications", codificationviews.CodificationList.as_view()),
    path("api/codifications/<int:pk>", codificationviews.CodificationDetail.as_view()),
    
]
urlpatterns = format_suffix_patterns(urlpatterns)