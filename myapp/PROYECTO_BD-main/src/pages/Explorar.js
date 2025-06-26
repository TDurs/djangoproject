import React from 'react';
import '../styles/Explorar.css';
import Navbar from '../components/Navbar';

export default function Explorar() {
  return (
    <>
      <Navbar />

      <header className="header">
        <div className="header-content container">
          <h1 style={{ color: '#1a1a1a' }}>MY BOOK HAVEN</h1>
          <p>
            Aquí encontrarás un espacio dedicado a tu pasión por los libros, 
            donde cada historia tiene un lugar especial. 
            Esta librería personal reúne títulos que te han acompañado, inspirado y transformado, 
            y quiero compartir contigo la magia que encierran sus páginas.
            Explora, descubre nuevas aventuras y déjate llevar por el poder de las palabras. 
            ¡Que cada visita sea el inicio de un nuevo viaje!
          </p>
        </div>
      </header>

      <section className="book">
        <img className="book-img" src="/imagenes/flores1.PNG" alt="" />

        <div className="book-content container">
          <h2>Explora nuestras colecciones</h2>
          <p className="txt-p">
            Sumérgete en un mundo de historias, conocimientos y aventuras. 
            Descubre los géneros literarios que han marcado épocas y 
            encuentra tu próxima lectura favorita.
          </p>

          <div className="book-group">
            <div className="book-1">
              <img src="/imagenes/dibujo1.jpg" alt="" />
              <h3>Novelas de Ficcion</h3>
              <p>
                Historias que despiertan la imaginación, nos transportan a mundos nuevos 
                y nos permiten vivir mil vidas en una sola.
              </p>
            </div>

            <div className="book-1">
              <img src="/imagenes/dibujo2.jpg" alt="" />
              <h3>Ciencia y conocimiento</h3>
              <p>
                Libros que abren la mente, explican el universo 
                y nos invitan a descubrir el fascinante mundo que nos rodea.
              </p>
            </div>

            <div className="book-1">
              <img src="/imagenes/dibujo3.jpg" alt="" />
              <h3>Poesia y ensayo</h3>
              <p>
                Palabras que tocan el alma 
                y reflexiones que nos invitan a mirar la vida desde nuevas perspectivas.
              </p>
            </div>
          </div>
        </div>
      </section>

      <main className="services">
        <div className="services-content container">
          <h2>Library services</h2>
          <div className="services-group">
            <div className="services-1">
              <img src="/imagenes/i1.svg" alt="" />
              <h3>Servicio 1</h3>
            </div>
            <div className="services-1">
              <img src="/imagenes/i2.svg" alt="" />
              <h3>Servicio 2</h3>
            </div>
            <div className="services-1">
              <img src="/imagenes/i3.svg" alt="" />
              <h3>Servicio 3</h3>
            </div>
          </div>
          <p>
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          </p>
        </div>
      </main>

      <section className="general">
        <div className="general-1">
          <h2>totam similique</h2>
          <p>
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          </p>
        </div>
        <div className="general-2"></div>
      </section>

      <section className="general">
        <div className="general-3"></div>
        <div className="general-1">
          <h2>totam similique</h2>
          <p>
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          </p>
        </div>
      </section>

      <section className="blog container">
        <h2>Blog</h2>
        <p>axxxxxxxxxxxxxxxxxxxxxxxxxxxxxx</p>
        <div className="blog-content">
          <div className="blog1">
            <img src="/imagenes/blog1.PNG" alt="" />
            <h3>Blog 1</h3>
            <p>
              zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
              zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
            </p>
          </div>
          <div className="blog1">
            <img src="/imagenes/blog1.PNG" alt="" />
            <h3>Blog 1</h3>
            <p>
              zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
              zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
            </p>
          </div>
          <div className="blog1">
            <img src="/imagenes/blog1.PNG" alt="" />
            <h3>Blog 1</h3>
            <p>
              zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
              zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
            </p>
          </div>
        </div>
      </section>

      <footer className="footer">
        <div className="footer-content container">
          <div className="link">
            <h3>lorem</h3>
            <ul>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
            </ul>
          </div>
          <div className="link">
            <h3>lorem</h3>
            <ul>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
            </ul>
          </div>
          <div className="link">
            <h3>lorem</h3>
            <ul>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
              <li><a href="#"></a></li>
            </ul>
          </div>
        </div>
      </footer>
    </>
  );
}
