# Class Name Checker

A simple Flask application that allows users to check for the presence of predefined CSS class names on a webpage. Users can submit a URL and select a class array to verify which classes are found on that page.

- **Predefined Class Names**: Supports multiple categories including Certificate, Letter, Visiting Card, Social Post, Greeting Card, ID Card, Invitation, and Menu Card.
- **User-Friendly Interface**: Simple form for inputting URLs and selecting class arrays.
- **Results Display**: Displays a table of results showing whether each class was found.

## Technologies Used

- Python
- Flask
- Beautiful Soup
- HTML/CSS

## Installation and Usage
Clone the repository: `git clone https://github.com/kalpesh9101/assignment-checker.git`, navigate to the project directory: `cd assignment-checker`, create and activate a virtual environment (optional): `python -m venv venv`, then on Windows run `venv\Scripts\activate` or on macOS/Linux run `source venv/bin/activate`, install the required packages: `pip install flask requests beautifulsoup4`, start the Flask application: `python app.py`, and open a web browser to `http://127.0.0.1:5000/` to enter the URL and select the class array before submitting the form to see the results.

Contributions are welcome! Please open an issue or submit a pull request.