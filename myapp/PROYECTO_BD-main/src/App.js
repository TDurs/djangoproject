import React, { useState } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Login';
import Explorar from './pages/Explorar';
import Coleccion from './pages/Coleccion';
import Perfil from './pages/Perfil';

export default function App() {
  const [loggedIn, setLoggedIn] = useState(false);

  if (!loggedIn) return <Login onLogin={() => setLoggedIn(true)} />;

  return (
    <Routes>
      <Route path="/" element={<Navigate to="/explorar" />} />
      <Route path="/explorar" element={<Explorar />} />
      <Route path="/coleccion" element={<Coleccion />} />
      <Route path="/perfil" element={<Perfil />} />
    </Routes>
  );
}
