import React from 'react';
import Navbar from '../components/Navbar';
import '../styles/Coleccion.css';

const librosEjemplo = [
  {
    id: 1,
    titulo: "1984",
    autor: "George Orwell",
    fechaPublicacion: 1949,
  },
  {
    id: 2,
    titulo: "Cien años de soledad",
    autor: "Gabriel García Márquez",
    fechaPublicacion: 1967,
  },
  {
    id: 3,
    titulo: "El principito",
    autor: "Antoine de Saint-Exupéry",
    fechaPublicacion: 1943,
  },
  {
    id: 4,
    titulo: "Rayuela",
    autor: "Julio Cortázar",
    fechaPublicacion: 1963,
  },
  {
    id: 5,
    titulo: "Fahrenheit 451",
    autor: "Ray Bradbury",
    fechaPublicacion: 1953,
  },
  {
    id: 6,
    titulo: "Orgullo y prejuicio",
    autor: "Jane Austen",
    fechaPublicacion: 1813,
  },
  {
    id: 7,
    titulo: "Don Quijote de la Mancha",
    autor: "Miguel de Cervantes",
    fechaPublicacion: 1605,
  },
  {
    id: 8,
    titulo: "Crónica de una muerte anunciada",
    autor: "Gabriel García Márquez",
    fechaPublicacion: 1981,
  },
  {
    id: 9,
    titulo: "Matar a un ruiseñor",
    autor: "Harper Lee",
    fechaPublicacion: 1960,
  },
  {
    id: 10,
    titulo: "La sombra del viento",
    autor: "Carlos Ruiz Zafón",
    fechaPublicacion: 2001,
  },
];

export default function Coleccion() {
  const [orden, setOrden] = React.useState('reciente');

  const librosOrdenados = [...librosEjemplo].sort((a, b) => {
    if (orden === 'alfabetico') {
      return a.titulo.localeCompare(b.titulo);
    } else if (orden === 'fecha') {
      return a.fechaPublicacion - b.fechaPublicacion;
    }
    return b.id - a.id; // más reciente
  });

  return (
    <>
      <Navbar />
      <div className="coleccion-container">
        <h2>Mi Colección de Libros</h2>

        <div className="filtro">
          <label>Ordenar por: </label>
          <select onChange={(e) => setOrden(e.target.value)} value={orden}>
            <option value="reciente">Más reciente</option>
            <option value="alfabetico">Alfabéticamente</option>
            <option value="fecha">Fecha de publicación</option>
          </select>
        </div>

        <div className="libros-grid">
          {librosOrdenados.map((libro) => (
            <div className="libro-card texto" key={libro.id}>
              <h3>{libro.titulo}</h3>
              <p>{libro.autor}</p>
              <p className="anio">({libro.fechaPublicacion})</p>
              <button>Ver más</button>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}
