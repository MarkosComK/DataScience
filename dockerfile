# Base image
FROM postgres:latest

# Environment variables for setup
ENV POSTGRES_DB=piscineds
ENV POSTGRES_USER=your_login
ENV POSTGRES_PASSWORD=mysecretpassword
