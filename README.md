# Trip Explorer

Welcome to Trip Explorer – your ultimate travel itinerary planner! Trip Explorer is a web application that helps users plan their travel adventures by selecting their preferences. The backend is powered by Django framework, REST APIs, Python, and MySQL, while the frontend utilizes HTML, CSS, and JavaScript.

## Features

- **Personalized Itineraries**: Users can input their preferences, including location, interests, budget, etc., to receive personalized travel itineraries.
- **Dynamic Itinerary Generation**: The backend processes user preferences and generates tailored travel plans, ensuring a memorable trip experience.
- **Intuitive User Interface**: Trip Explorer provides an intuitive and user-friendly interface for users to interact with and view their travel itineraries.
- **RESTful APIs**: The backend exposes RESTful APIs for handling user requests and fetching data from the MySQL database.

## Technologies Used

- **Backend**: Django framework, Django REST Framework, Python, MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Development Tools**: Git, GitHub

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/trip-explorer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd traveldatabase
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the MySQL database settings in `settings.py`:

    ```python
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel',
        'USER': 'root',
        'PASSWORD': 'physics@123',
        'HOST': '127.0.0.1',  
        'PORT': '3306',
    }
}
    ```

5. Run migrations to create database tables:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Trip Explorer website.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.


