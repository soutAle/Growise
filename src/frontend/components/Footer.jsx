import React from "react";
import { Link } from "react-router-dom";

export const Footer = () => {
    return (
        <footer className="bg-gray-900 text-gray-200 py-10">
            <div className="container mx-auto px-6 md:px-12">
                {/* Grid para distribución del contenido */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    {/* Sección: Acerca de */}
                    <div>
                        <h2 className="text-2xl font-bold text-white">Growise</h2>
                        <p className="mt-4 text-sm text-gray-400">
                            Conectamos talento con oportunidad.
                        </p>
                    </div>

                    {/* Sección: Enlaces útiles */}
                    <div>
                        <h3 className="text-lg font-semibold text-white mb-4">
                            Enlaces útiles
                        </h3>
                        <ul className="space-y-2 text-sm">
                            <li>
                                <Link to="/" className="hover:text-white">
                                    Inicio
                                </Link>
                            </li>
                            <li>
                                <Link to="/about" className="hover:text-white">
                                    Sobre nosotros
                                </Link>
                            </li>
                            <li>
                                <Link to="/home" className="hover:text-white">
                                    Inicio
                                </Link>
                            </li>
                        </ul>
                    </div>

                    {/* Sección: Redes sociales */}
                    <div>
                        <h3 className="text-lg font-semibold text-white mb-4">Síguenos</h3>
                        <div className="flex space-x-4">
                            {/* Íconos de redes sociales */}
                            <a
                                href="https://facebook.com"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="hover:text-blue-500"
                            >
                                <i className="fab fa-facebook fa-lg"></i>
                            </a>
                            <a
                                href="https://twitter.com"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="hover:text-blue-400"
                            >
                                <i className="fab fa-twitter fa-lg"></i>
                            </a>
                            <a
                                href="https://instagram.com"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="hover:text-pink-500"
                            >
                                <i className="fab fa-instagram fa-lg"></i>
                            </a>
                            <a
                                href="https://youtube.com"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="hover:text-red-500"
                            >
                                <i className="fab fa-youtube fa-lg"></i>
                            </a>
                        </div>
                    </div>
                </div>

                {/* Línea divisoria */}
                <div className="mt-8 border-t border-gray-700"></div>

                {/* Derechos de autor */}
                <div className="mt-6 text-center text-sm text-gray-500">
                    © 2025 MiLogo. Todos los derechos reservados.
                </div>
            </div>
        </footer>
    );
};

