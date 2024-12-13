# Likes and Notifications System API Documentation

This section covers the new **Likes** and **Notifications** functionalities added to the Social Media API. Users can like/unlike posts, and receive notifications about various actions such as likes, comments, and new followers.

---

## Like Post
### Endpoint
`POST /posts/<int:pk>/like/`

### Description
This endpoint allows a user to like a post. When a user likes a post, a notification is sent to the post's author.

### Request Example
```bash
POST /posts/5/like/
```
Headers:
```json
{
    "Authorization": "Bearer <access_token>"
}
```

### Response
On success:
```json
{
    "message": "Post liked successfully"
}
```

On failure (if the user has already liked the post):
```json
{
    "message": "You have already liked this post"
}
```

---

## Unlike Post
### Endpoint
`POST /posts/<int:pk>/unlike/`

### Description
This endpoint allows a user to unlike a post.

### Request Example
```bash
POST /posts/5/unlike/
```

### Response
On success:
```json
{
    "message": "Post unliked successfully"
}
```

On failure (if the user hasn’t liked the post yet):
```json
{
    "message": "You have not liked this post"
}
```

---

## Get Notifications
### Endpoint
`GET /notifications/`

### Description
This endpoint retrieves all notifications for the logged-in user. It will return both read and unread notifications.

### Request Example
```bash
GET /notifications/
```
Headers:
```json
{
    "Authorization": "Bearer <access_token>"
}
```

### Response
```json
{
    "notifications": [
        {
            "actor": "john",
            "verb": "liked your post",
            "target": "Test Post",
            "created_at": "2024-12-13T12:00:00Z",
            "is_read": false
        }
    ],
    "unread_count": 1
}
```

---

## Mark Notification as Read
### Endpoint
`POST /notifications/<int:pk>/read/`

### Description
This endpoint marks a specific notification as read.

### Request Example
```bash
POST /notifications/1/read/
```

### Response
```json
{
    "message": "Notification marked as read"
}
```

---

### How to Interact with the Like and Notification Features

1. **Liking a Post**: 
   - Use the `POST /posts/<int:pk>/like/` endpoint to like a post.
   - The post author will receive a notification indicating that you liked their post.
   
2. **Unliking a Post**: 
   - Use the `POST /posts/<int:pk>/unlike/` endpoint to unlike a post.
   - The like will be removed, and no further notifications will be sent for that action.

3. **Notifications**: 
   - Users can view all their notifications using the `GET /notifications/` endpoint.
   - To mark a notification as read, use the `POST /notifications/<int:pk>/read/` endpoint.

---

## Notes
- Make sure to include a valid authorization token in the header for authenticated requests.
- The notifications system is designed to handle different types of actions, including likes, comments, and follows. You can extend it to support more types of notifications as needed.
