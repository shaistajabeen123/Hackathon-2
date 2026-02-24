# Authentication API Endpoints

This document describes the authentication endpoints added to the Todo Backend API.

## Endpoints

### POST /api/v1/auth/register
Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user_id": "uuid-string"
}
```

### POST /api/v1/auth/login
Authenticate a user and return an access token.

**Request Body (form-data):**
- username: email address
- password: plain text password

**Response:**
```json
{
  "access_token": "jwt-token-string",
  "token_type": "bearer"
}
```

## Usage

After registering and logging in, use the returned access token in the Authorization header for protected endpoints:

```
Authorization: Bearer <access_token>
```

## Security

- Passwords are hashed using bcrypt
- Access tokens are JWTs with configurable expiration
- Email and username uniqueness is enforced
- All authentication flows are properly validated