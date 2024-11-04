from drf_yasg import openapi

# ---- Notes ----

# Documentation for creating a Note (POST)
create_note = {
    "description": "Create a new note for the authenticated user.",
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, example="My Note"),
            "content": openapi.Schema(type=openapi.TYPE_STRING, example="This is the content of my note."),
        },
        required=["title", "content"]
    ),
    "responses": {
        201: openapi.Response(
            description="Note created successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "title": openapi.Schema(type=openapi.TYPE_STRING, example="My Note"),
                    "content": openapi.Schema(type=openapi.TYPE_STRING, example="This is the content of my note."),
                    "author": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "created_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    "updated_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                }
            )
        ),
        400: "BAD_REQUEST: Invalid request data.",
        401: "Unauthorized: Authentication required."
    }
}

# Documentation for retrieving a Note (GET by ID)
retrieve_note = {
    "description": "Retrieve a note by its ID.",
    "responses": {
        200: openapi.Response(
            description="Note retrieved successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "title": openapi.Schema(type=openapi.TYPE_STRING, example="My Note"),
                    "content": openapi.Schema(type=openapi.TYPE_STRING, example="This is the content of my note."),
                    "author": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "created_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    "updated_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                }
            )
        ),
        404: "NOT_FOUND: Note not found.",
        401: "Unauthorized: Authentication required."
    }
}

# Documentation for listing all Notes (GET)
list_notes = {
    "description": "List all notes for the authenticated user.",
    "responses": {
        200: openapi.Response(
            description="Notes listed successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                        "title": openapi.Schema(type=openapi.TYPE_STRING, example="My Note"),
                        "content": openapi.Schema(type=openapi.TYPE_STRING, example="This is the content of my note."),
                        "author": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                        "created_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                        "updated_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    }
                )
            )
        ),
        401: "Unauthorized: Authentication required."
    }
}

# Documentation for updating a Note (PUT or PATCH)
update_note = {
    "description": "Update an existing note for the authenticated user.",
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "title": openapi.Schema(type=openapi.TYPE_STRING, example="Updated Note"),
            "content": openapi.Schema(type=openapi.TYPE_STRING, example="Updated content."),
        },
        required=["title"]
    ),
    "responses": {
        200: openapi.Response(
            description="Note updated successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "title": openapi.Schema(type=openapi.TYPE_STRING, example="Updated Note"),
                    "content": openapi.Schema(type=openapi.TYPE_STRING, example="Updated content."),
                    "author": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "created_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                    "updated_at": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME),
                }
            )
        ),
        400: "BAD_REQUEST: Invalid request data.",
        404: "NOT_FOUND: Note not found.",
        401: "Unauthorized: Authentication required."
    }
}

# Documentation for deleting a Note (DELETE)
destroy_note = {
    "description": "Delete a note by its ID.",
    "responses": {
        204: "No Content: Note deleted successfully.",
        404: "NOT_FOUND: Note not found.",
        401: "Unauthorized: Authentication required."
    }
}



# ---- Tags ----

# Documentation for creating a Tag (POST)
create_tag = {
    "description": "Create a new tag with a random color.",
    "request_body": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, example="Important"),
            "color": openapi.Schema(type=openapi.TYPE_STRING, example="#FF5733"),  # Color field
        },
        required=["name"]
    ),
    "responses": {
        201: openapi.Response(
            description="Tag created successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    "name": openapi.Schema(type=openapi.TYPE_STRING, example="Important"),
                    "color": openapi.Schema(type=openapi.TYPE_STRING, example="#FF5733"),
                }
            )
        ),
        400: "BAD_REQUEST: Invalid request data.",
        401: "Unauthorized: Authentication required."
    }
}

# Documentation for listing all Tags (GET)
list_tags = {
    "description": "List all tags.",
    "responses": {
        200: openapi.Response(
            description="Tags listed successfully.",
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "id": openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                        "name": openapi.Schema(type=openapi.TYPE_STRING, example="Important"),
                        "color": openapi.Schema(type=openapi.TYPE_STRING, example="#FF5733"),
                    }
                )
            )
        ),
        401: "Unauthorized: Authentication required."
    }
}
