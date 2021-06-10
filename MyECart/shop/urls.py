from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackingStatus"),
    path("search/",views.search,name="Search"),
    path("product/<int:myid>",views.productview,name="ProductView"),
    path("checkout/",views.checkout,name="Checkout"),
    path("login/",views.u_login,name="login"),
    path("logout/",views.u_logout,name="logout"),
    path("signup/",views.signup,name="signup"),
    path("guest/",views.guest,name="guest"),
    path("gabout/",views.gabout,name="GAboutUs"),
    path("gcontact/",views.gcontact,name="GContactUs"),
    path("gproductview/<int:myid>",views.gproductview,name="GProductView"),
    
]
