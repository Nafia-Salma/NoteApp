import React, { useState } from "react";
import "../styles/Note.css";
import deleteIcon from "../assets/delete.svg";
import editIcon from "../assets/edit.svg";
import api from "../api";

function Note({ note, onDelete }) {
    const [isEditing, setIsEditing] = useState(false);
    const [updatedTitle, setUpdatedTitle] = useState(note.title);
    const [updatedContent, setUpdatedContent] = useState(note.content);
    const formattedDate = new Date(note.created_at).toLocaleDateString("en-US");
    const tags = note.tags || [];

    const handleEditToggle = () => {
        setIsEditing(!isEditing);
    };

    const handleUpdate = (e) => {
        e.preventDefault(); // Prevent the default form submission behavior

        api
            .patch(`/api/notes/update/${note.id}/`, { title: updatedTitle, content: updatedContent })
            .then((res) => {
                console.log("Update Response:", res); // Log the response
                if (res.status === 200) {
                    alert("Note updated!");
                    setIsEditing(false); // Close the edit mode after updating
                } else {
                    alert("Failed to update note.");
                }
            })
            .catch((err) => {
                console.error("Update Error:", err); // Log any errors
                alert(err);
            });
    };

    return (
        <div className="note">
            {isEditing ? (
                <form onSubmit={handleUpdate}> {/* Use form to handle submission */}
                    <input
                        type="text"
                        value={updatedTitle}
                        onChange={(e) => setUpdatedTitle(e.target.value)}
                        className="note_text" // Editable title
                        placeholder="Title"
                        required
                    />
                    <textarea
                        value={updatedContent}
                        onChange={(e) => setUpdatedContent(e.target.value)}
                        className="note_text" // Editable content
                        placeholder="Content"
                        required
                    />
                    <input type="submit" value="save" />
                </form>
            ) : (
                <>
                    <p className="note_title">{updatedTitle}</p>
                    <p className="note_content">{updatedContent}</p>
                    <p className="note_tags">
                        {tags.map((tag, index) => (
                            <span key={index} className="tag">{tag}</span>
                        ))}
                    </p>
                    <p className="note_date">{formattedDate}</p>
                    <div className="note_footer">
                        <img
                            src={editIcon}
                            alt="Edit"
                            className="note-icon"
                            onClick={handleEditToggle}
                        />
                        <img
                            src={deleteIcon}
                            alt="Delete"
                            className="note-icon"
                            onClick={() => onDelete(note.id)}
                        />
                    </div>
                </>
            )}
        </div>
    );
}

export default Note;
