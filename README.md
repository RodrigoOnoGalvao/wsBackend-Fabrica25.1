# wsBackend-Fabrica25.1

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/wsBackend-Fabrica25.1.git
    cd wsBackend-Fabrica25.1
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the application at `http://127.0.0.1:8000/`.
- Use the admin interface at `http://127.0.0.1:8000/admin/` to manage people and currencies.

## Docker

To run the application using Docker:

1. Build the Docker image:
    ```sh
    docker build -t wsbackend-fabrica25.1 .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 8000:8000 wsbackend-fabrica25.1
    ```
