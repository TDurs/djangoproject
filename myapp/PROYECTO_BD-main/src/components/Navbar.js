import React from 'react';
import { NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav style={styles.nav}>
      <div style={styles.logo}>📚 Mi Biblioteca</div>
      <div style={styles.links}>
        <NavLink to="/explorar" style={({ isActive }) => isActive ? { ...styles.link, ...styles.active } : styles.link}>Explorar</NavLink>
        <NavLink to="/coleccion" style={({ isActive }) => isActive ? { ...styles.link, ...styles.active } : styles.link}>Mi colección</NavLink>
        <NavLink to="/perfil" style={({ isActive }) => isActive ? { ...styles.link, ...styles.active } : styles.link}>Mi perfil</NavLink>
      </div>
      <input
        type="text"
        placeholder="Buscar libros..."
        style={styles.search}
      />
    </nav>
  );
}

const styles = {
  nav: {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: '#f4f1ea',
    padding: '10px 20px',
    borderBottom: '1px solid #ccc',
    fontFamily: 'Arial, sans-serif',
  },
  logo: {
    fontWeight: 'bold',
    fontSize: '20px',
    color: '#372213',
  },
  links: {
    display: 'flex',
    gap: '15px',
  },
  link: {
    textDecoration: 'none',
    color: '#372213',
    fontSize: '16px',
  },
  active: {
    fontWeight: 'bold',
    borderBottom: '2px solid #372213',
  },
  search: {
    padding: '6px 10px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    fontSize: '14px',
  },
};
