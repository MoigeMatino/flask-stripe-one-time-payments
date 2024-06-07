# Flask Stripe Payments

This repository contains a Flask application that seamlessly integrates Stripe to facilitate one-time payments using the checkout strategy. It offers a clear and concise implementation, providing a robust starting point for integrating Stripe's payment processing capabilities into your Flask projects. Whether you're building a simple e-commerce site or a more complex application, this example will help you quickly set up and customize Stripe payments to suit your needs.

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Usage](#usage)
5. [Database Migrations](#database-migrations)
6. [Extending the Project](#extending-the-project)
7. [Contributing](#contributing)
8. [License](#license)

## Project Description

This project demonstrates how to integrate Stripe into a Flask application for handling one-time payments. The implementation includes secure payment processing using Stripe Checkout, making it easier to add payment capabilities to your Flask applications.

## Features

- **Stripe Integration**: Easily integrate Stripe for handling one-time payments.
- **Secure Payments**: Utilize Stripe’s secure payment processing.
- **Extensible Codebase**: Designed to be easily extended for additional payment-related features.
- **Configuration Management**: Handle configuration through a dedicated endpoint.
- **Webhooks**: Receive and handle real-time notifications from Stripe for various events (e.g., payment success).
- **Dockerized Setup**: Run the application and database using Docker containers.
- **Database Migrations**: Use Flask-Migrate to handle database migrations.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Stripe account (with API keys)
  * [Create Stripe Account](https://dashboard.stripe.com/register) then navigate to the [dashboard](https://dashboard.stripe.com/test/dashboard),
    then click 'Developers'.


### Installation

1. **Clone the repository**:

    Using HTTPS:
    ```bash
    git clone https://github.com/yourusername/flask-stripe-payments.git
    cd flask-stripe-payments
    ```

    Using SSH:
    ```bash
    git clone git@github.com:yourusername/flask-stripe-payments.git
    cd flask-stripe-payments
    ```

2. **Set up your Stripe API keys and other environment variables**:

    Create a `docker.env` file in the root directory and add your Stripe keys and other environment variables e.g:

    ```env
    STRIPE_PUBLISHABLE_KEY=your_publishable_key
    STRIPE_SECRET_KEY=your_secret_key
    STRIPE_ENDPOINT_SECRET=your_webhook_endpoint_secret
    POSTGRES_DB=your_postgres_database
    ```

3. **Build and run the Docker containers**:

    ```bash
    docker-compose up --build
    ```

    This will start the Flask application and a PostgreSQL database in Docker containers.

## Usage

1. **Access the application**: Open your browser and go to `http://127.0.0.1:5000/`.

2. **Make a payment**: Click the "Purchase Supa Tee" button and complete the payment using the Stripe Checkout page.

## Database Migrations

To handle database migrations using Flask-Migrate, follow these steps:

1. **Create a migration script**:

    ```bash
    docker-compose exec flask_app flask db migrate -m "Initial migration."
    ```

2. **Apply the migration**:

    ```bash
    docker-compose exec flask_app flask db upgrade
    ```

These commands should be run inside the Docker container since the database is hosted there.

## Extending the Project

- **Add Subscriptions**: Implement subscription-based payments using Stripe.
- **Multiple Payment Methods**: Extend the payment options to include more methods supported by Stripe.
- **Sending Emails**: Send payment confirmation emails to customers.
- **Update Order Status**: Update the status of orders in the database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
