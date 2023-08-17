from django.urls import path
from blog_app.views import *

urlpatterns = [
    path('category/', CategoryView.as_view(), name="category_list"),
    path('add_category/', CategoryCreateView.as_view(), name="add_category"),
    path('category/<int:id>/', BlogCategoryView.as_view(), name="filtered_blog_list"),
    path('blog/', BlogListView.as_view(), name="blog_list"),
    path('blog/<int:id>/', BlogDetailView.as_view(), name="blog_post"),
    path('create_post/', BlogCreateView.as_view(), name="create_blog"),
]