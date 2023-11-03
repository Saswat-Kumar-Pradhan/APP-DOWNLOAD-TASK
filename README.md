# App Download Task

<div align="right">

[Watch the Screeccast Here](https://github.com/Saswat-Kumar-Pradhan/APP-DOWNLOAD-TASK/blob/main/screencast%20of%20app-download-task.mp4)

</div>

<div align="center">

#### A functioning web app (documentation)

</div>

## Project Overview

<ul>
    <li><strong>Project Name:</strong> Android App Download Task</li>
    <li><strong>Author:</strong> Saswat Kumar</li>
    <li><strong>Language:</strong> Python</li>
    <li><strong>Framework:</strong> Django (Frontend and Backend)</li>
    <li><strong>Frontend:</strong> HTML, CSS, JavaScript, Bootstrap
    </li>
    <li><strong>Backend:</strong> Python (Django)</li>
    <li><strong>Authentication:</strong> Custom Authentication using cookies</li>
    <li><strong>Session Management:</strong> Django Sessions</li>
</ul>

## Project Description

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The "Android App Download Task" project is a web application that allows users to download Android applications with the provided link. It provides a user-friendly interface to complete the task by uploading the proof which is screenshot of the opened application.After completing the task user scores the point which was fixed by the admin.

## Features

<ul>
    <li><strong>User Authentication:</strong>
        <ul>
            <li>Users can create accounts and log in to download and complete the tasks to score points.</li>
            <li>Custom authentication (using cookies) system is used for user management.</li>
        </ul>
    </li>
    <li><strong>App Listings:</strong>
        <ul>
            <li>Apps are added with points by the admin based on their type and sub-type.</li>
            <li>Users can browse and view details of each app and download the app to gain points.</li>
        </ul>
    </li>
    <li><strong>Download Functionality:</strong>
        <ul>
            <li>Authenticated users can download apps to their devices and upload the screenshot to complete the task.</li>
        </ul>
    </li>
    <li><strong>Responsive Design:</strong>
        <ul>
            <li>Bootstrap framework is implemented for responsive user interface.</li>
        </ul>
    </li>
</ul>

## Project Structure

    app-download-task/
    ├── app/
    │   ├── admin.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── views.py
    │   └── ...
    ├── static/
    │   ├── css/
    │   └── ...
    ├── templates/
    │   └── ...
    ├── media/
    │   └── ...
    ├── main/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── ...
    ├── manage.py
    └── db.sqlite3

## Installation and Setup 

<ol>
<li>Clone the Repository:</li><br>

```
git clone https://gitlab.com/saswatkumar059/django-evaluation-task.git
```
<li>Create a Virtual Environment:</li><br>
    
```
python3 -m venv env
```
<li>Activate the Virtual Environment:</li><br>
for Linux/MAC --
    
```
source env/bin/activate
```
for Windows --
```
env\Scripts\activate 
```
<li>Install Dependencies:</li><br>
    
```
pip install -r requirements.txt
```
<li>Apply Migrations:</li><br>
    
```
python3 manage.py migrate
```
<li>Run the Development Server:</li><br>
    
```
python3 manage.py runserver
```
</ol>

## Usage

<ul>
    <li><strong>User Registration and Login:</strong>
        <ul>
            <li>Users can create accounts or log in if they already have one.</li>
        </ul>
    </li>
    <li><strong>Create Task:</strong>
        <ul>
            <li>Admin can add an Android app as well as the number of points earned by a user for downloading the app.</li>
        </ul>
    </li>
    <li><strong>Complete the Task:</strong>
        <ul>
            <li>Users can download the app to complete the task (and upload a screenshot for proof).</li>
        </ul>
    </li>
    <li><strong>User Details:</strong>
        <ul>
            <li>Users can view their profile, total points earned, and a list of all completed tasks.</li>
        </ul>
    </li>
</ul>

## Screenshots

Login Page & Signup Page

<div style="display:flex;">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-45-01.png" alt="Screenshot" width="49%">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-45-13.png" alt="Screenshot" width="49%">
</div>

<br><br>
Admin Dashboard & Add task page

<div style="display:flex;">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-45-36.png" alt="Screenshot" width="49%">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-45-44.png" alt="Screenshot" width="49%">
</div>

<br><br>
User Dashboard & User Task Completion page

<div style="display:flex;">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-45-58.png" alt="Screenshot" width="49%">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-49-36.png" alt="Screenshot" width="49%">
</div>


<br><br>
User profile & User points

<div style="display:flex;">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-47-03.png" alt="Screenshot" width="49%">
    <img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-52-58.png" alt="Screenshot" width="49%">
</div>


<br><br>
User total task completed page

<img src="https://gitlab.com/trial-group6760842/trial-project/-/raw/main/screenshorts/Screenshot_from_2023-10-23_00-54-29.png" alt="Screenshot" width="49%">

## Conclusion

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The "Android App Download Task" project provides a user-friendly platform for users to download Android applications and complete the prospective tasks. With authentication and session management, it ensures secure access and interaction with the platform. The responsive design ensures a seamless experience on multiple devices.
<br><br><br><br>
<div align="center">
