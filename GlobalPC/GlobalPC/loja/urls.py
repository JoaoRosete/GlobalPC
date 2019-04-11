from django.conf.urls import url
from . import views
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)


urlpatterns = [
    # /loja/inicio/
    url(r'^inicio/$', views.loja, name='loja'),
    # /loja/product/product_id
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
    # /loja/subcategory/subcategory_id
    url(r'^subcategory/(?P<subcategory_id>[0-9]+)/$', views.subcategory, name='subcategory'),
    # loja/category/category_id
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category_subcategory_allproducts, name='category'),
    # /loja/login/
    url(r'^login/$', LoginView.as_view(template_name='loja/login.html'), name='login'),
    # /loja/logout/
    url(r'^logout/$', LogoutView.as_view(template_name='loja/logout.html'), name='logout'),
    # /loja/registar/
    url(r'^registar/$', views.register, name="register"),
    # /loja/perfil/
    url(r'^perfil/$', views.profile, name="profile"),
    # /loja/perfil/editar
    url(r'^perfil/editar/$', views.editar, name="edit"),
    # /loja/perfil/editar/mudar-password
    url(r'^perfil/editar/mudar-password/$', views.change_password, name="change_password"),
    # /loja/restframework-links/
    url(r'^restframework-links/$', views.restframework_links, name="restframework_links"),
    # /loja/inserir/
    url(r'^inserir/$', views.insert, name="insert"),
    # /loja/inserir/producto
    url(r'^inserir/producto/$', views.insert_product, name="insert_product"),
    # /loja/inserir/categoria
    url(r'^inserir/categoria/$', views.insert_category, name="insert_category"),
    # /loja/inserir/categoria
    url(r'^inserir/subcategoria/$', views.insert_subcategory, name="insert_subcategory"),
    #  /loja/compras-feitas
    url(r'^compras-feitas/$', views.purchases, name="purchases"),



    # Rest API
    url(r'^api/productos/$', views.ProductList.as_view(), name='product_list'),
    url(r'^api/categorias/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^api/subcategorias/$', views.SubCategoryList.as_view(), name='subcategory_list'),

    # Products, Categories, SubCategories -> Details
    url(r'^api/productos/(?P<pk>[0-9]+)/$', views.ProductDetails.as_view(), name='product_details'),
    url(r'^api/categorias/(?P<pk>[0-9]+)/$', views.CategoryDetails.as_view(), name='category_details'),
    url(r'^api/subcategorias/(?P<pk>[0-9]+)/$', views.SubCategoryDetails.as_view(), name='subcategory_details'),

]