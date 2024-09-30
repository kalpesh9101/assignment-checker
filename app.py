from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Predefined class name arrays
class_arrays = {
    'Certificate': ["certificate-content", "certificate-wrapper", "certificate-background", "title", "sr-no", "date", "subtitle", "initial-content", "candidate-name", "main-content", "sign-president-img", "sign-president", "sign-director-img", "sign-director", "org-logo", "org-name", "org-address"],
    'Letter': ["letter-content","letter-wrapper", "letter-background",  "letter-header", "letter-org-logo", "logoimg", "letter-ref", "letter-date", "letter-body", "letter-body-to", "letter-body-subject", "letter-body-salutation", "letter-body-message", "letter-body-sign-img", "letter-body-sign", "letter-footer", "letter-org-phone", "letter-org-email", "letter-org-website", "letter-org-address"],
    'Visiting': ["card-content", "name", "job-title", "company", "contact-info", "phone", "email", "address", "card-wrapper", "card-background"],
    'Social Post': ["content-wrapper","socialpost-wrapper", "socialpost-background",  "org-logo", "org-tagline", "org-address", "heading-first", "heading", "sub-heading", "description"],
    'Greeting Card': ["greeting-content","greeting-wrapper", "greeting-background",  "greeting-recipient-name", "greeting-heading", "greeting-sub-heading", "greeting-pre-message", "greeting-message", "greeting-closing-message", "greeting-sender-name", "greeting-personal-note"],
    'I Card': ["id-card-content", "id-card-wrapper-front", "id-card-background", "org-logo", "user-photo", "user-name", "id-number", "id-title", "org-name", "org-address", "id-card-wrapper-back", "qr-code", "id-emergency-contact", "id-blood-group", "id-dob", "id-issue-date", "id-expiry-date", "id-policy"],
    'Invitation': ["invitation-content","invitation-wrapper", "invitation-background",  "salutation", "tagline", "event-name", "date", "time", "location", "event-subheading", "event-pre-description", "event-description"],
    'Menu Card': ["restaurant-add-content","menu-wrapper", "menu-background",  "restaurant-phone", "restaurant-web", "restaurant-email", "menu-content", "restorent-name", "menu-list-group", "menu-list-heading", "menu-list", "menu-list-item"]
}

# Home route to display the form
@app.route('/')
def index():
    return render_template('index.html', class_arrays=class_arrays)

# Function to recursively check all nested divs for extra classes
def check_extra_classes(soup, allowed_classes,parentClass):
    extra_classes = []

    # Find all divs with class 'content'
    content_divs = soup.find_all(class_=parentClass)

    # Traverse each content div and its child elements
    for content_div in content_divs:
        for child_div in content_div.find_all('div', recursive=True):  # Recursive search for nested divs
            child_classes = child_div.get('class', [])
            for child_class in child_classes:
                # If the class is not allowed and is not 'content', consider it an extra class
                if child_class != parentClass and child_class not in allowed_classes:
                    extra_classes.append(f"Extra class '{child_class}' found inside '{parentClass}' div.")

    return extra_classes

# Route to handle the form submission and process the URL
@app.route('/check-classes', methods=['POST'])
def check_classes():
    url = request.form['url']
    selected_array = request.form['class_array']

    # Get the class names array based on user selection
    class_names = class_arrays.get(selected_array, [])

    try:
        # Fetch the page content
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        # Check for class names and store results
        results = []
        extra_class_errors = check_extra_classes(soup, class_names,class_names[0])

        # Loop over predefined class names to check if they exist
        for class_name in class_names:
            found = soup.find_all(class_=class_name)
            results.append({
                'class_name': class_name,
                'found': 'Yes' if found else 'No'
            })

        # Render the results in table format
        return render_template('results.html', url=url, results=results, extra_class_errors=extra_class_errors)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
