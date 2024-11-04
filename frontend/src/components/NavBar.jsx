import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Offcanvas from 'react-bootstrap/Offcanvas';
import '../styles/NavBar.css';
import myIcon from '../assets/avatar.jpeg';

function OffcanvasExample() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary mb-3">
      <Container fluid>
        <Navbar.Brand href="#" className="d-flex align-items-center">
          <img
            src={myIcon}
            alt="My Icon"
          />
          <span>Current Username</span> {/* Replace with your actual username */}
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="offcanvasNavbar" className="ms-auto" />
        <Navbar.Offcanvas
          id="offcanvasNavbar"
          aria-labelledby="offcanvasNavbarLabel"
          placement="end"
        >
          <Offcanvas.Header closeButton>
            <Offcanvas.Title id="offcanvasNavbarLabel">Menu</Offcanvas.Title>
          </Offcanvas.Header>
          <Offcanvas.Body>
            <Nav className="justify-content-end flex-grow-1 pe-3">
              <Nav.Link href="/">Home</Nav.Link>
              <Nav.Link href="/login">Login</Nav.Link>
              <Nav.Link href="/logout">Logout</Nav.Link>
              <Nav.Link href="/register">Register</Nav.Link>
              <Nav.Link href="/notFound">Not Found</Nav.Link>
            </Nav>
          </Offcanvas.Body>
        </Navbar.Offcanvas>
      </Container>
    </Navbar>
  );
}

export default OffcanvasExample;
