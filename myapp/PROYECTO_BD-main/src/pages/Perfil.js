import React, { useState } from 'react';
import '../styles/Perfil.css';
import Navbar from '../components/Navbar';

export default function Perfil() {
  const [editando, setEditando] = useState(false);
  const [nombre, setNombre] = useState('Nombre del Usuario');
  const [correo, setCorreo] = useState('usuario@ejemplo.com');

  const [nuevoNombre, setNuevoNombre] = useState(nombre);
  const [nuevoCorreo, setNuevoCorreo] = useState(correo);

  const guardarCambios = () => {
    setNombre(nuevoNombre);
    setCorreo(nuevoCorreo);
    setEditando(false);
  };

  return (
    <>
      <Navbar />
      <div className="perfil-container">
        <div className="perfil-card">
          <img
            className="perfil-foto"
            src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
            alt="Foto de perfil"
          />

          {editando ? (
            <>
              <input
                type="text"
                value={nuevoNombre}
                onChange={(e) => setNuevoNombre(e.target.value)}
                className="perfil-input"
              />
              <input
                type="email"
                value={nuevoCorreo}
                onChange={(e) => setNuevoCorreo(e.target.value)}
                className="perfil-input"
              />
              <p><strong>Miembro desde:</strong> enero 2024</p>
              <p><strong>Libros leídos:</strong> 12</p>
              <p><strong>Favoritos:</strong> El Principito, 1984</p>
              <button className="perfil-boton" onClick={guardarCambios}>Guardar</button>
            </>
          ) : (
            <>
              <h2 className="perfil-titulo">{nombre}</h2>
              <p><strong>Correo:</strong> {correo}</p>
              <p><strong>Miembro desde:</strong> enero 2024</p>
              <p><strong>Libros leídos:</strong> 12</p>
              <p><strong>Favoritos:</strong> El Principito, 1984</p>
              <button className="perfil-boton" onClick={() => setEditando(true)}>Editar Perfil</button>
            </>
          )}
        </div>
      </div>
    </>
  );
}
