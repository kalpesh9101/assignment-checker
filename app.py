from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Predefined class name arrays
class_arrays = {
    'Certificate': ["certificate-wrapper","certificate-background","certificate-content", "title", "sr-no", "date", "subtitle", "initial-content", "candidate-name", "main-content", "sign-president-img", "sign-president", "sign-director-img", "sign-director", "org-logo", "org-name", "org-address"],
    'Letter':  ["letter-wrapper","letter-background","letter-content", "letter-header", "letter-org-logo", "logoimg", "letter-ref", "letter-date", "letter-body", "letter-body-to", "letter-body-subject", "letter-body-salutation", "letter-body-message", "letter-body-sign-img", "letter-body-sign", "letter-body-sign", "letter-footer", "letter-org-phone", "letter-org-email", "letter-org-website", "letter-org-address"],
    'Visiting':["card-content", "name", "job-title", "company", "contact-info", "phone", "email", "address", "card-wrapper", "card-background"],
    'Social Post':["socialpost-wrapper", "socialpost-background", "content-wrapper", "org-logo", "org-tagline", "org-address", "org-alternate-email", "org-phone", "org-phone1", "org-alternate-phone", "org-fax", "heading-first", "heading", "sub-heading", "description", "punchline-1", "punchline-2", "offerline-1", "offerline-2", "services-heading", "services", "service", "service-name", "service-image", "service-description", "contact-us", "contact", "Location", "Location-image", "features-heading", "feature-imagee", "features", "feature", "feature-name1", "feature-image1", "feature-name2", "feature-image2", "feature-name3", "feature-image3", "feature-name4", "feature-image4", "feature-name5", "feature-image5", "feature-name6", "feature-image6", "feature-name7", "feature-image7", "terms-heading", "term-image-MEMBERSHIP", "terms", "term", "term-name", "term-image1", "term-image2", "term-image3", "term-image-MEMBERSHIP1", "footer", "org-website", "org-email", "org-name", "term-description"],
    'Greeting Card':["greeting-wrapper", "greeting-background", "greeting-content", "greeting-recipient-name", "greeting-heading", "greeting-sub-heading", "greeting-pre-message", "greeting-message", "greeting-closing-message", "greeting-sender-name", "greeting-personal-note", "greeting-date", "greeting-occasion", "greeting-image", "greeting-additional-image", "greeting-special-instructions"],
    'I Card':["id-card-wrapper-front", "id-card-background", "id-card-content", "org-logo", "user-photo", "user-name", "id-number", "id-title", "org-name", "org-address", "id-card-wrapper-back", "qr-code", "id-emergency-contact", "id-blood-group", "id-dob", "id-issue-date", "id-expiry-date", "id-policy"],
    'Invitation':["invitation-wrapper", "invitation-background", "invitation-content", "salutation", "tagline", "event-name", "date", "time", "location", "event-subheading", "event-pre-description", "event-description", "event-participant-1", "event-participant-1-details", "event-participant-2", "event-participant-2-details", "event-organizer", "event-other-organizers", "event-organizers-contact-person", "event-organizers-contact-number"],
    'Menu Card':["menu-wrapper", "menu-background", "restaurant-add-content", "restaurant-phone", "org-phone-lable", "org-phone-number", "restaurant-web", "org-web-lable", "org-web-address", "restaurant-email", "org-email-lable", "org-email-address", "menu-content", "restorent-name", "restorent-discription", "menu-list-group", "menu-list-heading", "menu-list-image", "menu-list", "menu-list-item", "menu-list-item-name", "menu-list-item-price", "menu-list-image2"]
}

# Home route to display the form
@app.route('/')
def index():
    return render_template('index.html', class_arrays=class_arrays)

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
        for class_name in class_names:
            found = soup.find_all(class_=class_name)
            results.append({
                'class_name': class_name,
                'found': 'Yes' if found else 'No'
            })

        # Render the results in table format
        return render_template('results.html', url=url, results=results)

    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
