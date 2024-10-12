<a id="readme-top"></a>
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Github][github-shield]][github-url]

# Newsfeed App

This project is a simple newsfeed application that allows users to create posts, comment, like, share, and follow other
users. The backend is built using Flask and connects to a MySQL database.

## Table of Contents

1. [Project Structure](#Project-Structure)
1. [Prerequisites](#Prerequisites)
2. [Installation](#Setup-Instructions)
3. [SQL Code](#SQL-code)
6. [ERD schema](#ERD-schema)

## Project Structure

- `app/`: Contains the core Flask application with all routes and business logic.
- `.env`: Environment variables.
- `run.py`: Entry point for running the Flask application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prerequisites

- Python 3.x
- MySQL

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/eslam5464/news-feed.git
   cd news-feed/backend

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Set up the MySQL database:
    - Make sure you have a MySql database set up -> [Download MySql][mysql-download-url]
    - Run the db_query.sql script located in the root directory to create the required tables
      ```bash
      mysql -u root -p < fixtures/db_query.sql
      ```

4. Start the Flask app:
   ```bash
   python run.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## SQL code

- located inside the repo -> [MySql script path][sql-script-url]

## ERD schema

![ERD Diagram][erd-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[mysql-download-url]: https://dev.mysql.com/downloads/

[github-url]: https://github.com/eslam5464/news-feed

[github-shield]: https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge

[linkedin-url]: https://linkedin.com/in/eslam5464

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[erd-url]: https://raw.githubusercontent.com/eslam5464/news-feed/refs/heads/master/backend/fixtures/erd.png

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[license-url]: https://github.com/eslam5464/news-feed/blob/master/LICENSE

[sql-script-url]: https://github.com/eslam5464/news-feed/blob/master/backend/fixtures/db_query.sql