<h2>Project Summary</h2><hr>

This project was built to fully understand the basis of authentications and CRUD operations. The auth_app in the api handles all authentications while the blog_app handles the CRUD operations.

<h2>Project Instructions</h2><hr>
Enter these into the command line
<ul>
	<h3>Installation</h3>
	<li>'git clone https://www.github.com/AdemiluaAdeola/django_blog_api.git'</li>
	<li>'python3 -m pip install -r requirements.txt'</li>
	<li>'python manage.py makemigrations'</li>
	<li>'python manage.py migrate'</li>
	<h3>Creating Admin</h3>
	<li>'python manage.py createsuperuser'</li>
	<h3>Run Server</h3>
	<li>'python manage.py runserver'</li>
</ul>

<h2>Endpoints</h2>
<ul>
	<h3>Blog app Endpoints</h3>
	<li>'localhost:8000/admin/' - This endpoint handles the admin dashboard</li>
	<li>'http://127.0.0.1:8000/api/category/' - This endpoint retrieves all blog categories from the database</li>
	<li>'http://127.0.0.1:8000/api/add_category/' - This endpoint is used to create a new category</li>
	<li>'http://127.0.0.1:8000/api/category/id/' - This endpoint retrieves all blog posts related to the category;the id must be a positive integer</li>
	<li>'http://127.0.0.1:8000/api/blog/' - This endpoint retrieves all blog posts on the server</li>
	<li>'http://127.0.0.1:8000/api/blog/id/' - This endpoint retrieves the blog post with the id. It also allows the user to edit or delete the post if the user is the owner of 	the post or a staff/admin user</li>
	<li>'http://127.0.0.1:8000/api/create_post/' - This endpoint creates new blog posts</li>
	<h3>Authentication/User Endpoints</h3>
	<li>'http://127.0.0.1:8000/api_auth/login/' - This endpoint receives login details from the end user and validates it in the authentication system set up in the backend</li>
	<li>'http://127.0.0.1:8000/api_auth/register' - This endpoint creates a new user in the database</li>
	<li>'http://127.0.0.1:8000/api_auth/change_password/id/' - This endpoint retrieves and updates the user's passwords</li>
	<li>'http://127.0.0.1:8000/api_auth/update_profile/id/' - This endpoint retrieves and updates the user's profiles</li>
	<li>'http://127.0.0.1:8000/api_auth/profile/' - This endpoint retrieves the user's profiles</li>
</ul>
