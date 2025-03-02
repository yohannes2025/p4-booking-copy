# Restaurant Booking System

![Home_Page](static/images/home.png)

## CONTENTS
- [Site Objectives](#site-objectives)
- [User Experience/UX](#user-experienceux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
    - [New Visitor Goals](#new-visitor-goals)
    - [Existing Visitor Goals](#existing-visitor-goals)
- [Design Choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Logo and Favicon](#logo-and-favicon)
  - [Wireframes](#wireframes)
  - [Flow Diagram](#flow-diagram)
  - [Database Plan](#database-plan)
- [Features](#features)
  - [Registration](#registration)
  - [Future Features](#future-features)
  - [Features Not Included](#features-not-included)
- [Technologies Used](#technologies-used)
- [Programming Languages, Frameworks and Libraries Used](#programming-languages-frameworks-and-libraries-used)
- [Agile](#agile)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [User](#user)
  - [Bugs](#bugs)
  - [Lighthouse](#lighthouse)
  - [Validation Testing](#validation-testing)
    - [HTML & CSS](#html--css)
  - [Python Testing](#python-testing)
- [Deployment](#deployment)
  - [Github Deployment](#github-deployment)
  - [Creating a Fork or Copying](#creating-a-fork-or-copying)
  - [Clone](#clone)
  - [Repository deployment via Heroku](#repository-deployment-via-heroku)
  - [Deployment of the app](#deployment-of-the-app)
- [Credits](#credits)
- [Media](#media)
- [Acknowledgments and Thanks](#acknowledgments-and-thanks)


## Site Objectives
The Restaurant Booking System aims to provide users with an easy and efficient way to book tables at their favorite restaurants. It eliminates the need for direct phone calls and enables customers to manage their bookings effortlessly online, enhancing overall customer satisfaction.
*   **Simplify the Reservation Process** – Allow customers to book tables online, view available time slots, and receive instant confirmation.
    
*   **Improve Restaurant Management** – Help restaurant staff track reservations, manage peak hours, and minimize overbooking.
    
*   **Enhance Customer Experience** – Provide a user-friendly interface for customers to make, modify, or cancel bookings effortlessly.
    
*   **Optimize Table Utilization** – Ensure better occupancy rates by dynamically managing reservations.
    
*   **Enable Secure and Efficient Communication** – Send automated confirmation emails, reminders, and notifications to both customers and staff.
    
*   **Support Multi-Branch Operations** (if applicable) – Allow users to choose locations if the restaurant has multiple branches.
    
*   **Integrate with Authentication & User Management** – Enable customer login via **Django Allauth** for a personalized experience.
    
*   **Scalability & Deployment** – Ensure smooth deployment on **Heroku**, supporting future scalability.

## User Experience/UX

### Target Audience
The target audience for this application includes:
1. **Diners**:
   * **Food Enthusiasts**: Individuals looking to try new dining experiences, cuisines, and venues.
   * **Families**: Parents seeking a convenient way to book tables for family outings.
   * **Corporate Clients**: Professionals needing to arrange business lunches or dinners at restaurants.
   * **Tourists**: Travelers wanting to discover local dining options and make reservations in advance.
   * **Event Planners**: Individuals organizing events such as parties or gatherings requiring specific arrangements.
2. **Restaurant Owners and Managers**:
   * **Small to Medium-Sized Restaurant Owners**: Owners looking for an efficient way to manage bookings and customer interactions.
   * **Restaurant Managers**: Personnel responsible for day-to-day operations and customer service, aimed at improving efficiency.
3. **Staff Members**:
   * **Waitstaff and Hosts**: Employees needing access to booking systems to manage seating arrangements and customer flow.

- Diners looking to book tables in advance.
- Restaurant owners who want to manage bookings more efficiently.
- Users who appreciate a seamless online experience for reservations.

**User Stories**

**New Visitor Goals**

1. **As a new visitor**, I want to easily navigate the website so that I can quickly find a restaurant that meets my preferences.
2. **As a new visitor**, I want to view detailed information about each restaurant (menu, photos, reviews) so that I can make an informed decision.
3. **As a new visitor**, I want to create an account quickly and securely so that I can save my preferences for future visits.
4. **As a new visitor**, I want to receive confirmation of my reservation via email or SMS so that I have a record of it.
5. **As a new visitor**, I want to see special offers or promotions to take advantage of potential discounts.

**Existing Visitor Goals**

1. **As an existing visitor**, I want to log in to my account easily so that I can access my previous reservations and preferences.
2. **As an existing visitor**, I want to modify or cancel my reservations without complications to manage my plans effectively.
3. **As an existing visitor**, I want to receive notifications about upcoming reservations so that I can prepare in advance.
4. **As an existing visitor**, I want to provide feedback or leave reviews based on my dining experience to help improve the restaurant's service.
5. **As an existing visitor**, I want to access loyalty rewards and promotions that apply to returning guests to encourage further bookings.


## Design Choices

### Colour Scheme

The chosen color scheme aims to evoke a warm and inviting atmosphere while maintaining clarity and usability. The primary colors are:


### Typography

The typography choices focus on readability and aesthetic appeal. The selected fonts are:

- **Font**: Arial, Helvetica, sans-serif, sans-serif - Used for headings and body text for a modern and clean appearance. It improves readability across various devices.

**Font Sizes**:
- Headings: 24px (H1), 20px (H2), 18px (H3)
- Body Text: 16px

### Wireframes

Wireframes provide a blueprint of the user interface, outlining the basic layout and functionality without concentrating on visual design.

- **Home Page Wireframe**: Features sections like restaurant search, special offers, and top-rated restaurants.
- **Reservation Page Wireframe**: Displays a form for date, time, number of guests, and special requests.
- **Profile Page Wireframe**: Allows users to view and edit their profiles and reservation history.


### Flow Diagram

The flow diagram illustrates the user journey through the Restaurant Booking System, depicting how users interact with the application’s features.

- **User Registration/Login**: First-time users register while returning users log in to access their accounts.
- **Restaurant Search**: Users search for restaurants based on various criteria (location, cuisine, rating).
- **Reservation Process**: Users select a restaurant, choose a date/time, and confirm the reservation.
- **Confirmation/Feedback**: Users receive a confirmation email and can leave feedback after their dining experience.


### Database Plan

1. **Project Planning & Requirements Gathering**

* **Dataset Definition:**

**Tables:**

* + Restaurant: restaurant\_id (INT, PRIMARY KEY, AUTO\_INCREMENT),
  + restaurant\_name (VARCHAR),
  + address (VARCHAR), phone\_number (VARCHAR),
  + Table: table\_id (INT, PRIMARY KEY, AUTO\_INCREMENT),
  + restaurant\_id (INT, FOREIGN KEY referencing Restaurant),
  + table\_number (VARCHAR - can be a combination like "Table 1A"),
  + capacity (INT - number of guests the table can accommodate)
  + MenuItem: menu\_item\_id (INT, PRIMARY KEY, AUTO\_INCREMENT),
  + restaurant\_id (INT, FOREIGN KEY referencing Restaurant),
  + item\_name (VARCHAR),
  + Booking: booking\_id (INT, PRIMARY KEY, AUTO\_INCREMENT),
  + restaurant\_id (INT, FOREIGN KEY referencing Restaurant),
  + user\_id (INT, FOREIGN KEY referencing Django's built-in User model or a custom Customer model – explained below),
  + table\_id (INT, FOREIGN KEY referencing Table),
  + booking\_date (DATE),
  + booking\_time (TIME),
  + number\_of\_guests (INT),
  + customer\_name (VARCHAR),
  + customer\_email (VARCHAR),
* **Relationships:**

Clear one-to-many relationships between Restaurant and Table, Restaurant and MenuItem, Restaurant and Booking, Table and Booking, User and Booking. MenuItem belongs to a Restaurant. Customer has one-to-one relationship with User.

* **User Roles & Permissions:**
  + Customer/Guest:
    - Can view the restaurant's details, menu.
    - Can make a booking.
    - Can view and cancel their own bookings.
  + Restaurant Owner/Manager:
    - Full access to the site.
    - Can add, edit, and delete restaurant details (name, address, hours).
    - Can manage tables (add, edit, delete).
    - Can manage the menu (add, edit, delete menu items).
    - Can view and manage all bookings (accept/confirm, cancel, mark as completed, etc.).
    - Can see reports.
  + Staff Member (optional ):
    - Limited access. Can be able to view bookings for the day, mark bookings as completed, but not make changes to the restaurant's settings or the menu.
* **User Interface (UI) & Features:**
  + **Customer/Guest-Facing Pages:**
    - **Home/Landing Page:** Restaurant details (name), contact information.
    - **Menu Page:** Display the menu items, organized by category.
    - **Booking Form:**
      * Date selection (using a date picker).
      * Time selection (dropdown or time picker – consider business hours).
      * Number of guests selection.
      * Table selection (optional).
      * Customer name, phone number, email (required fields).
    - **My Bookings Page:** (If user accounts are implemented) List all bookings for the user, with options to view details and cancel.
  + **UI Considerations:**
    - **Responsive Design:** Bootstrap is used which is essential for mobile users.
    - **Calendar/Time Selection:** Appropriate UI widgets used (e.g., a calendar for date selection, a time picker or a time dropdown).
    - **Clear Information Display:** Ensure that booking information and restaurant details are easy to read and understand.

1. **Database Design (MySQL or PostgreSQL)**

* **Schema Definition:** (As defined in the Dataset Definition section above)
  + Tables: Restaurant, Table, MenuItem, Booking, and User (or Customer)
* **Database Connection:** In settings.py.
* **ORM (Object-Relational Mapper) and Models (in inventory/models.py ):**

1. **Django Backend Development**

* **Project and App Setup:** Similar to the previous example.
* **Models (in restaurant/models.py):** (See above)
* **Admin Interface:** Register models in restaurant/admin.py
* **Authentication:** Django's built-in authentication. A Package django-allauth has been used
* **User Roles & Permissions:** The administrator can give permissions to users based on the roles, e.g., can\_manage\_bookings, can\_manage\_menu, can\_view\_restaurant\_details.


## Features

This document outlines the key features of the Restaurant Booking System, designed to enhance user experience for diners, restaurant owners, and managers.

---

## Key Features

### For Diners

1. **User Registration and Authentication**:
   - Users can create an account and securely log in to access features tailored to their preferences.
   - Password recovery options are available for users who forget their login credentials.

2. **Restaurant Search**:
   - Users can search for restaurants based on various criteria including location, cuisine type, and rating.
   - Filters to narrow down search results based on price range, distance, and availability.

3. **Detailed Restaurant Profiles**:
   - Each restaurant has a dedicated profile page featuring:
     - Menu options
     - Photos
     - Customer reviews and ratings
     - Contact information

4. **Reservation Management**:
   - Users can easily book tables for desired dates and times.
   - Users are allowed to modify or cancel reservations through their profiles.
   - Confirmation emails and notifications are sent after booking or changes.

5. **User Profiles**:
   - Users can maintain profiles with personal information, view reservation history, and save favorite restaurants.
   - Options to provide feedback and leave reviews for dine-in experiences.

6. **Promotions and Discounts**:
   - Users can access special offers and promotions available at various restaurants.
   - Loyalty rewards for returning customers to encourage repeat business.

### For Restaurant Owners and Managers

1. **Restaurant Management Dashboard**:
   - Owners and managers can manage restaurant details, including operating hours, menu items, and pricing.
   - Analytics dashboard to view reservation statistics, peak times, and customer feedback.

2. **Reservation Handling**:
   - Monitor real-time reservations and manage table allocations.
   - Send confirmation emails to customers and manage waiting lists if necessary.

3. **Customer Feedback**:
   - Ability to view and respond to customer reviews.
   - Insights into customer satisfaction to improve service quality.

4. **Promotions Management**:
   - Create and manage promotional offers and discounts to attract more diners.
   - Track the performance of promotions through analytics.

### For Staff Members

1. **Staff Login**: 
   - Waitstaff and hosts can log in to access booking schedules and manage seating arrangements.

2. **Order Management Integration**:
   - Integrated with order management systems to ensure staff can efficiently manage their workflow during service.

### General Features

1. **Mobile Responsiveness**:
   - Designed to provide an optimal experience across all devices, including smartphones, tablets, and desktops.

2. **Accessibility Features**:
   - The application incorporates accessibility standards (WCAG) to ensure it is usable for individuals with disabilities.

3. **Data Security**:
   - User data is encrypted and appropriately secured to protect personal and payment information.

4. **Contact and Support**:
   - An integrated support system for users to reach out for help with reservations, technical issues, or inquiries.

## Technologies Used

This document lists the technologies, frameworks, programming languages, and tools utilized in the development of the Restaurant Booking System.

---
## Agile
Agile methodologies were employed throughout development, with an emphasis on iterative progress, continuous feedback, and adaptability to change. Regular sprint reviews and retrospectives were conducted to refine processes.

---

## Frontend Technologies

1. **HTML5**:
   - Used for structuring the content of the web application, ensuring semantic and accessible markup.

2. **CSS3**:
   - Utilized for styling the user interface, implementing responsive design practices, and managing layout to enhance user experience.

3. **Bootstrap** :
   - A front-end framework used for developing responsive and mobile-first websites quickly and efficiently.

---

## Backend Technologies

1. **Django**:
   - Django is a high-level Python web framework that simplifies the development of secure, scalable, and maintainable web applications. It follows the Model-View-Template (MVT) architecture and comes with built-in features that help developers build web applications quickly and efficiently.

4. **Database Management System**:
   - **PstgreSQL** 
     - PostgreSQL (often called Postgres) is a powerful, open-source, object-relational database system (ORDBMS) known for its reliability, extensibility, and performance. It is widely used in web applications, data analytics, and large-scale enterprise solutions..

---

## Development and Tools

1. **Version Control**:
   - **Git**: 
     - Used for source code management, allowing developers to track changes, collaborate, and manage different versions of the codebase.
   - **GitHub**: 
     - Used for hosting the repository, facilitating collaboration, code reviews, and issue tracking.

2. **Development Environment**:
   - **Visual Studio Code** (or other code editors):
     - A lightweight, powerful code editor with integrated debugging, syntax highlighting, and extensions to enhance productivity.

---

## Deployment

1. **Heroku** :
   - A cloud platform used for deploying the application, providing easy scaling and management of server resources.


## Testing

The Restaurant Booking System uses the following testing frameworks and tools:

### Django Test Framework:
  - For unit testing and integration testing in the backend. This is part of Django's built-in testing capabilities.
  
### Manual testing:
  - Each feature was manually tested to ensure functionality and a seamless user experience.
  

 ### Testing Program:
  - A separate tests.py python program is written for testing Restaurant, Table, Booking creation and validation.No problem was found.
 
### User test
User testing was conducted with a group to receive feedback on usability and overall satisfaction.

### Bugs
Regular debugging sessions were held, and issues were tracked in the GitHub repository.

### Lighthouse
Performance audits were conducted using Google Lighthouse, focusing on speed and accessibility.

![Alt text](static/images/lighthouse.png)

  
---

## Types of Tests

1. **Unit Tests**:
   - Tests specific components or functions in isolation to ensure they behave as expected.
   - Example: Testing model methods, view logic, or utility functions.

2. **Integration Tests**:
   - Tests the interaction between different components, such as how views interact with models or how API endpoints work with the frontend.
  
3. **Functional Tests**:
   - Tests the application from the user's perspective, simulating user actions and validating end-to-end workflows.

4. **API Tests**:
   - Specific tests focusing on the API endpoints to verify their correctness, including status codes, response body, and performance.
  
5. **Performance Tests**:
   - These tests check how the application performs under various levels of load.

---



### Validation Testing
#### HTML & CSS
All HTML and CSS were validated using the W3C Validator to ensure conformance with web standards.

![CSS Validation](static/images/css_validation.png)


#### Python Testing
Unit tests were created using Django's testing framework to validate models and views.

## Credits
Developed by [Your Name], using open-source resources and libraries.

## Media
Images and media used within the app are sourced from royalty-free websites and credited appropriately.

## Acknowledgments and Thanks
Special thanks to all contributors and the user testing team whose feedback enhanced the project.

## Deployment
### Github Deployment
The project is hosted on GitHub, allowing collaborative development and version control.

### Creating a Fork or Copying
Users can fork the repository to contribute or create a copy for personal use.

### Clone
To clone the repository, run:
```bash
git clone https://pp4restaurant-booking-system-a622aad68454.herokuapp.com/


