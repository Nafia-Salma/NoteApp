import { useState, useEffect } from "react";
import api from "../api";
import Note from "../components/Note";
import "../styles/Home.css";
import plusIcon from "../assets/plus.svg";
import { Modal, Button, Form } from 'react-bootstrap';

function Home() {
    const [notes, setNotes] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");
    const [showModal, setShowModal] = useState(false);

    useEffect(() => {
        getNotes();
    }, []);

    const getNotes = () => {
        api
            .get("/api/notes/")
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
            })
            .catch((err) => alert(err));
    };

    // Function to delete a note by its ID
    const deleteNote = (id) => {
        api
            .delete(`/api/notes/destroy/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Note deleted!");
                else alert("Failed to delete note.");
                getNotes();
            })
            .catch((error) => alert(error));
    };

    // Function to create a new note
    const createNote = ({ title, content, tags }) => {
        api
            .post("/api/notes/", { title, content, tags })
            .then((res) => {
                if (res.status === 201) {
                    alert("Note created!");
                    setTitle("");
                    setContent("");
                    setShowModal(false);
                } else {
                    alert("Failed to make note.");
                }
                getNotes();
            })
            .catch((err) => alert(err));
    };

    // Function to open the modal for creating a note
    const handleAddNoteClick = () => {
        setShowModal(true);
    };

    // Function to close the modal
    const handleCloseModal = () => {
        setShowModal(false);
    };

    return (
        <div>
            <div className="notes-header">
                <h2>Notes</h2>
                <button className="add-button" onClick={handleAddNoteClick}>
                    <img src={plusIcon} alt="Add Note" />
                </button>
            </div>
            <div className="notes-section">
                {notes.map((note) => (
                    <Note note={note} onDelete={deleteNote} key={note.id} />
                ))}
            </div>

            {/* Modal for Creating a Note */}
            <NoteModal
                showModal={showModal}
                handleCloseModal={handleCloseModal}
                createNote={createNote}
            />
        </div>
    );
}

// Separate component for NoteModal
function NoteModal({ showModal, handleCloseModal, createNote }) {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [tags, setTags] = useState([]);
    const [selectedTags, setSelectedTags] = useState([]);
    const [newTag, setNewTag] = useState('');

    useEffect(() => {
        const fetchTags = async () => {
            try {
                const response = await api.get('/api/tags/');
                setTags(response.data);
            } catch (error) {
                console.error('Error fetching tags:', error);
            }
        };
        fetchTags();
    }, []);

    const handleTagSelection = (e) => {
        const value = Array.from(e.target.selectedOptions, option => option.value);
        setSelectedTags(value);
    };

    const handleAddTag = async () => {
        if (newTag.trim()) {
            try {
                const response = await api.post('/api/tags/', { name: newTag });
                const createdTag = response.data;
                setTags([...tags, createdTag]);
                setSelectedTags([...selectedTags, createdTag.id]);
                setNewTag('');
            } catch (error) {
                console.error('Error creating new tag:', error);
            }
        }
    };

    const handleFormSubmit = (e) => {
        e.preventDefault();
        createNote({
            title,
            content,
            tags: selectedTags,
        });
        setTitle('');
        setContent('');
        setSelectedTags([]);
        handleCloseModal();
    };

    return (
        <Modal show={showModal} onHide={handleCloseModal}>
            <Modal.Header closeButton>
                <Modal.Title>Create Note</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <form onSubmit={handleFormSubmit}>
                    <div className="mb-3">
                        <label htmlFor="title" className="form-label">Title:</label>
                        <input
                            type="text"
                            id="title"
                            className="form-control"
                            required
                            onChange={(e) => setTitle(e.target.value)}
                            value={title}
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="content" className="form-label">Content:</label>
                        <textarea
                            id="content"
                            className="form-control"
                            required
                            value={content}
                            onChange={(e) => setContent(e.target.value)}
                        ></textarea>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="tags" className="form-label">Tags:</label>
                        <Form.Select
                            id="tags"
                            className="form-control"
                            multiple
                            value={selectedTags}
                            onChange={handleTagSelection}
                        >
                            {tags.map(tag => (
                                <option key={tag.id} value={tag.id}>{tag.name}</option>
                            ))}
                        </Form.Select>
                    </div>
                    <div className="mb-3 d-flex">
                        <input
                            type="text"
                            className="form-control me-2"
                            placeholder="Add new tag"
                            value={newTag}
                            onChange={(e) => setNewTag(e.target.value)}
                        />
                        <Button variant="outline-primary" onClick={handleAddTag}>
                            Add
                        </Button>
                    </div>
                    <Button type="submit" variant="primary">Submit</Button>
                </form>
            </Modal.Body>
        </Modal>
    );
}

export default Home;
