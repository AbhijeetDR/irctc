# IRCTC Project

## Project Overview

This project is a simplified implementation of the Indian Railways Catering and Tourism Corporation (IRCTC) system. It provides a set of APIs to manage user authentication, train management, and ticket booking.

## Features

- User Signup: Users can create an account by providing their details.
- User Login: Registered users can log in using their credentials.
- Add New Train: Admins can add new trains to the system.
- Book Ticket: Registered users can book tickets for available trains.
- Seat Availability: Users can check seat availability from source to destination.
- Get Specific Booking Detail: Users can retrieve details about their booked tickets.

## Tech Stack

- **Framework**: Django
- **Database**: SQLite (Please note that MySQL was not used in this implementation)
- **Authentication**: Django's built-in authentication system
- **API Development**: Django Views

## API Endpoints

1. **Signup**:
   - [POST] `/api/signup/`

2. **Login**:
   - [POST] `/api/login/`

3. **Add New Train**:
   - [POST] `/api/trains/create`

4. **Book a Seat**:
   - [POST] `/api/trains/<int:train_id>/book`

5. **Seat Availability from Source to Destination**:
   - [GET] `/api/trains/availability/?source=SOURCE&destination=DESTINATION`

6. **Get Specific Booking Detail**:
   - [GET] `/api/bookings_id/<int:booking_id>/`

