import React from 'react'
import { Link } from "react-router-dom";

export const Navbar = () => {
    return (
        <nav className="bg-gray-900 text-gray-200 shadow-lg">
            <div className="container mx-auto align-center px-4">
                <div className="flex justify-center items-end py-4">
                    <div className="text-2xl font-bold mx-2">
                        <Link to="/" className="hover:text-gray-300">
                            Growise
                        </Link>
                    </div>
                    <ul className="flex space-x-10 ms-10">
                        <li>
                            <Link to="/" className="hover:text-gray-300 transition duration-200">
                                Inicio
                            </Link>
                        </li>
                        <li>
                            <Link to="/about" className="hover:text-gray-300 transition duration-200">
                                Sobre nosotros
                            </Link>
                        </li>
                        <li>
                            <Link to="/login" className="hover:text-gray-300 transition duration-200">
                                Login
                            </Link>
                        </li>
                        <li>
                            <Link to="/signup" className="hover:text-gray-300 transition duration-200">
                                Signup
                            </Link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};