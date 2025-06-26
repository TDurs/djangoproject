import React from 'react';

export default function Login({ onLogin }) {
  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Iniciar Sesión</h2>
      <input type="text" placeholder="Usuario" style={styles.input} />
      <input type="password" placeholder="Contraseña" style={styles.input} />
      <button style={styles.button} onClick={onLogin}>Entrar</button>
    </div>
  );
}

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f4f1ea',
    fontFamily: 'Arial, sans-serif',
  },
  title: {
    marginBottom: '20px',
    color: '#372213',
  },
  input: {
    padding: '10px',
    margin: '8px 0',
    borderRadius: '4px',
    border: '1px solid #ccc',
    width: '200px',
    fontSize: '14px',
  },
  button: {
    padding: '10px 20px',
    backgroundColor: '#372213',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    fontSize: '14px',
    cursor: 'pointer',
    marginTop: '10px',
  },
};