# Social Media API Documentation

This API allows users to manage posts and comments on a social media platform. It provides the ability to create, view, update, and delete posts and comments.

---

## **Post Endpoints**

### 1. **Create a New Post**
- **Endpoint**: `POST /posts/`
- **Description**: Allows authenticated users to create a new post.
- **Request**:
  - **Method**: POST
  - **URL**: `/posts/`
  - **Body** (JSON format):
    ```json
    {
      "title": "My New Post",
      "content": "This is the content of the post"
    }
    ```
  - **Authorization**: Requires authentication (API token or login credentials).
  
- **Response**:
  - **Status Code**: 201 Created
  - **Body** (JSON):
    ```json
    {
      "id": 1,
      "author": "john_doe",
      "title": "My New Post",
      "content": "This is the content of the post",
      "created_at": "2024-12-13T12:00:00Z",
      "updated_at": "2024-12-13T12:00:00Z"
    }
    ```
  
- **Error Handling**:
  - **400 Bad Request**: Missing required fields or invalid data.
  - **401 Unauthorized**: If the user is not authenticated.

---

### 2. **Get All Posts**
- **Endpoint**: `GET /posts/`
- **Description**: Retrieve a paginated list of all posts.
- **Request**:
  - **Method**: GET
  - **URL**: `/posts/`
  - **Query Parameters** (optional):
    - `search`: Filter posts by title or content.
    - `ordering`: Sort posts by `created_at`.
    - Example: `/posts/?search=python&ordering=created_at`
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "count": 5,
      "next": "http://api.example.com/posts/?page=2",
      "previous": null,
      "results": [
        {
          "id": 1,
          "author": "john_doe",
          "title": "My New Post",
          "content": "This is the content of the post",
          "created_at": "2024-12-13T12:00:00Z",
          "updated_at": "2024-12-13T12:00:00Z"
        }
      ]
    }
    ```

- **Error Handling**:
  - **404 Not Found**: No posts exist.

---

### 3. **Get a Specific Post**
- **Endpoint**: `GET /posts/{id}/`
- **Description**: Retrieve a single post by its ID.
- **Request**:
  - **Method**: GET
  - **URL**: `/posts/{id}/` (e.g., `/posts/1/`)
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "id": 1,
      "author": "john_doe",
      "title": "My New Post",
      "content": "This is the content of the post",
      "created_at": "2024-12-13T12:00:00Z",
      "updated_at": "2024-12-13T12:00:00Z"
    }
    ```
  
- **Error Handling**:
  - **404 Not Found**: If the post with the specified ID does not exist.

---

### 4. **Update a Post**
- **Endpoint**: `PUT /posts/{id}/`
- **Description**: Update an existing post (only by the post’s author).
- **Request**:
  - **Method**: PUT
  - **URL**: `/posts/{id}/`
  - **Body** (JSON format):
    ```json
    {
      "title": "Updated Title",
      "content": "Updated content"
    }
    ```
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "id": 1,
      "author": "john_doe",
      "title": "Updated Title",
      "content": "Updated content",
      "created_at": "2024-12-13T12:00:00Z",
      "updated_at": "2024-12-13T13:00:00Z"
    }
    ```
  
- **Error Handling**:
  - **400 Bad Request**: If the data is invalid.
  - **403 Forbidden**: If the user is not the author.

---

### 5. **Delete a Post**
- **Endpoint**: `DELETE /posts/{id}/`
- **Description**: Delete a post (only by the post’s author).
- **Request**:
  - **Method**: DELETE
  - **URL**: `/posts/{id}/`
  
- **Response**:
  - **Status Code**: 204 No Content
  - **Body**: No content (empty response).
  
- **Error Handling**:
  - **403 Forbidden**: If the user is not the author.

---

## **Comment Endpoints**

### 1. **Create a New Comment**
- **Endpoint**: `POST /comments/`
- **Description**: Allows authenticated users to create a new comment on a post.
- **Request**:
  - **Method**: POST
  - **URL**: `/comments/`
  - **Body** (JSON format):
    ```json
    {
      "post": 1,
      "content": "Great post!"
    }
    ```
  - **Authorization**: Requires authentication.
  
- **Response**:
  - **Status Code**: 201 Created
  - **Body** (JSON):
    ```json
    {
      "id": 1,
      "author": "john_doe",
      "post": 1,
      "content": "Great post!",
      "created_at": "2024-12-13T12:30:00Z",
      "updated_at": "2024-12-13T12:30:00Z"
    }
    ```

---

### 2. **Get All Comments**
- **Endpoint**: `GET /comments/`
- **Description**: Retrieve all comments for a specific post.
- **Request**:
  - **Method**: GET
  - **URL**: `/comments/?post={post_id}`
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "count": 2,
      "results": [
        {
          "id": 1,
          "author": "john_doe",
          "content": "Great post!",
          "created_at": "2024-12-13T12:30:00Z"
        }
      ]
    }
    ```

---

### 3. **Update a Comment**
- **Endpoint**: `PUT /comments/{id}/`
- **Description**: Update a comment (only by the comment’s author).
- **Request**:
  - **Method**: PUT
  - **URL**: `/comments/{id}/`
  - **Body** (JSON):
    ```json
    {
      "content": "Updated comment content"
    }
    ```
  
- **Response**:
  - **Status Code**: 200 OK
  - **Body** (JSON):
    ```json
    {
      "id": 1,
      "author": "john_doe",
      "post": 1,
      "content": "Updated comment content",
      "created_at": "2024-12-13T12:30:00Z"
    }
    ```

---

### 4. **Delete a Comment**
- **Endpoint**: `DELETE /comments/{id}/`
- **Description**: Delete a comment (only by the comment’s author).
- **Request**:
  - **Method**: DELETE
  - **URL**: `/comments/{id}/`
  
- **Response**:
  - **Status Code**: 204 No Content
  - **Body**: Empty response.

---

## **Error Handling**

- **400 Bad Request**: Invalid data, missing required fields, or malformed request.
- **401 Unauthorized**: Missing or invalid authentication token.
- **403 Forbidden**: If the user is not authorized to perform the action (e.g., not the author of the post/comment).
- **404 Not Found**: When the resource (post/comment) is not found.
- **405 Method Not Allowed**: If the HTTP method used is not supported for the resource.

---

### **Authentication**
- All endpoints (except for GET requests that don’t require authentication) require user authentication.
- The API uses **JWT** or **OAuth** for authentication.

---

### **Rate Limiting**
- Rate limits are applied to prevent abuse. You can make up to **100 requests per hour**.

---

### **Versioning**
- Current version: **v1**
- Future versions will be added to support backward compatibility.

# User Follows and Feed API Documentation

This documentation outlines the **User Follows** and **Feed** functionalities added to the Social Media API. These features allow users to follow and unfollow other users, and view an aggregated feed of posts from the users they follow.

---

## Endpoints Overview

- **Follow a User**: `POST /follow/<int:user_id>/`
- **Unfollow a User**: `POST /unfollow/<int:user_id>/`
- **View Feed**: `GET /feed/`

---

## 1. Follow User

### Endpoint
`POST /follow/<int:user_id>/`

### Description
This endpoint allows a user to follow another user. After 
