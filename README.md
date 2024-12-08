# PostgreSQL Database Project

This project sets up a PostgreSQL database for managing sales data and customer information. It's structured to handle data analysis and data engineering tasks.

## Prerequisites

Before you begin, ensure you have the following installed:
- Docker
- Docker Compose
- PostgreSQL client (for psql commands)

## Project Structure

```
piscine_db/
├── ex00/              # Database setup
├── ex01/              # Database visualization
├── ex02/              # First table creation
├── ex03/              # Automatic table creation
├── ex04/              # Items table
├── dockerfile
├── docker-compose.yml
├── .gitignore
├── .dockerignore
└── README.md
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/MarkosComK/DataScience
cd DataScience
```

2. Set up the database (Exercise 00):
```bash
docker-compose up -d
cd ex00
```

3. Verify the connection:
```bash
# Replace 'your_login' with your actual login
psql -U your_login -d piscineds -h localhost -W
```
When prompted, enter the password: `mysecretpassword`

## Configuration

The PostgreSQL database is configured with:
- Database name: `piscineds`
- Username: your login
- Password: mysecretpassword
- Port: 5432

## Exercises Overview

### Exercise 00: Database Setup
- Sets up PostgreSQL using Docker
- Creates initial database and user

### Exercise 01: Database Visualization
- Configure visualization tools for database management

### Exercise 02: First Table
- Create and populate first table from CSV data

### Exercise 03: Automatic Table Creation
- Automatically create tables from CSV files

### Exercise 04: Items Table
- Create and configure items table

## Troubleshooting

If you encounter connection issues:
1. Ensure Docker is running
2. Check if the container is up:
```bash
docker-compose ps
```
3. View container logs:
```bash
docker-compose logs
```

## Stopping the Project

To stop the database:
```bash
docker-compose down
```

To stop and remove all data:
```bash
docker-compose down -v
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
