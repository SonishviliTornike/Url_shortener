# URL Shortener

Author: Tornike Sonishvili  
Email: sonishvili.tornike@gmail.com  
Phone: 577 777 353

## Overview

URL Shortener is a web application built to shorten long URLs into concise, shareable links. It provides an easy and efficient way to manage URLs effectively.

## Features

- **URL Shortening**: Convert long URLs into shorter, more manageable links.
- **Custom Short URLs**: Customize shortened URLs for branding or readability.
- **Link Analytics**: Track the usage and performance of shortened links.
- **User Authentication**: Secure access with user authentication and authorization.
- **Admin Dashboard**: Manage URLs, view analytics, and user activity through an intuitive admin interface.

## Installation

To run the URL Shortener locally, follow these steps:

1. **Clone the repository:**
   git clone <repository_url>

2. **Navigate to the project directory:**
   cd URL-Shortener

3. **Set up a virtual environment (optional but recommended):**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

4. **Install dependencies:**
   pip install -r requirements.txt

5. **Apply database migrations:**
   python manage.py migrate

6. **Run the development server:**
   python manage.py runserver

7. **Access the application in your web browser at: http://localhost:8000**

## Usage
1. Sign up for an account or log in if you already have one.
2. Once logged in, enter a long URL into the provided form.
3. Optionally customize the shortened URL slug.
4. Click "Shorten" to generate a shortened URL.
5. View and manage your shortened URLs in your dashboard.

## How It Works
Users can input long URLs into the application.
The application generates a unique, shortened URL for each input URL.
Users can share the shortened URL, which redirects to the original long URL when accessed.
The application tracks usage statistics and provides analytics for each shortened URL
