# Budget Tracker
#### Video Demo:  <https://drive.google.com/file/d/1nqm_-eT6-RZykWTcPCzrv9GSV1HTZBt4/view?usp=sharing>
#### Description:

In today's fast-paced world, efficient financial management is essential. Having a solid system in place may be quite beneficial, whether you're tracking personal spending or controlling the finances of your business. The Budget Tracker online application can help with that. This application, built on the robust Flask framework, has a simple user interface and powerful to help you with your financial management.

The Model-View-Controller (MVC) model is used in the application architecture. The models.py file defines the models, which use SQLAlchemy ORM to manage database interactions. Flask is used to manage the display logic and routing for views and controllers, which are implemented in the views.py file.

## Features

### User Authentication

- User authentication features are provided by the Budget Tracker online application, guaranteeing the safety and security of user accounts. 
- Users can log in with their email address and password or create a new account.

#### Account Creation

- By entering email address and selecting a secure password, new users can quickly create an account.
- The Werkzeug library, a popular Python password hashing package, is used to safely hash passwords. By doing this, it is made sure that passwords are kept in the database and hidden from view by administrators as well.

#### Secure Login

- After creating an account, users can sign in with their password and email address.
- In order to reduce the possibility of unwanted access, the program uses secure authentication methods to confirm the user's credentials.

### Transaction Management

Whether tracking revenue or keeping track of spending, the Budget Tracker program gives customers the ability to handle their financial operations effectively.

#### Adding Transactions

- It is simple for users to add new income transactions or expenses. All they have to do is mention the transaction's amount, category, and month.
- In order to ensure appropriate spending categorization, customers can select from predefined categories when entering expenses, including housing, transportation, food, healthcare, entertainment, and more.
- Users can see their transaction history at any moment thanks to the database's storage of transactions.

#### Viewing Transaction History

- Consumers have access to their transaction history, which offers an extensive overview of all of their financial transactions.  
- Users can track their revenue and expenses over time by viewing important facts about their transactions, including the month, amount, category, and kind of transaction (income or expense).

### Responsive Design

The adaptable design of the Expense Tracker online application offers a smooth user experience on a variety of screens and devices.

#### Bootstrap Integration

- Bootstrap, a popular front-end framework, is used to design a responsive and visually appealing user interface.
- Desktops, laptops, tablets, and smartphones may all use the application because of its optimal layout and style.

### Data Visualization

The Budget Tracker application's home page offers customers informative data visualization elements that improve their comprehension of their financial situation.

#### Summary of Financial Metrics

- On the home page, users may see a summary of their total earnings, total expenses, and remaining budget for the chosen month. 
- By giving consumers a brief summary of their financial condition, these metrics assist users in making wise choices regarding their spending and saving practices.


#### Pie Chart Representation

- In addition, a pie chart provides customers with a straightforward visual representation of their spending patterns by displaying expenses by category.
- The pie chart shows categories including housing, transportation, food, entertainment, and healthcare, enabling users to pinpoint areas where they might need to make expenditure adjustments.

## Usage

- Sign up for a new account or log in with an existing account.
- Add new expenses or income transactions by specifying the amount, category, and month.
- View your transaction history to see a list of all your past transactions.
- Delete any transaction from your history if needed.

## Technologies Used

- Flask: Python's lightweight web framework.
- SQLAlchemy: A database interaction library for Object-Relational Mapping (ORM).
- Bootstrap: A responsive design and layout front-end framework.
- Chart.js: An interactive graphing and charting JavaScript library.
- Werkzeug: A library for security-related operations, such as hashing passwords.
- HTML and CSS: Used to organize and style online pages.
- JavaScript: For dynamic content and client-side interaction.

## Conclusion 

Budget Tracker is an online application that simplifies money management duties for both individuals and enterprises. Its features include robust user identification, complete transaction management, flexible design, and analytical data visualization. Whether you're keeping track of personal spending or managing business money, the Budget Tracker gives you the power to take charge of your financial future.

This project was developed by Adeliya Tislova as part of CS50.

