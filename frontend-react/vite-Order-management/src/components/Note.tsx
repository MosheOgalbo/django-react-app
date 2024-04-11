import React from "react";
import "../styles/Note.css";

interface NoteProps {
  note: {
    id: number; // Assuming ID is a number
    title: string;
    content: string;
    created_at: string; // Assuming created_at is a string representing a date
  };
  onDelete: (id: number) => void; // Function to handle delete with ID argument
}

function Note({ note, onDelete }: NoteProps) {
  const formattedDate = new Date(note.created_at).toLocaleDateString("en-US");

  return (
    <div className="note-container">
      <p className="note-title">{note.title}</p>
      <p className="note-content">{note.content}</p>
      <p className="note-date">{formattedDate}</p>
      <button className="delete-button" onClick={() => onDelete(note.id)}>
        Delete
      </button>
    </div>
  );
}

export default Note;
