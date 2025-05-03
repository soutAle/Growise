import React, { useState } from "react";
import axios from "axios";
import { useDispatch } from "react-redux";
import { loginSuccess } from "../authSlice";
import { useNavigate } from "react-router-dom";

export const SignUpFormComponent = () => {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(null);

    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleSignUp = async (e) => {
        e.preventDefault();

        try {
            const res = await axios.post("http://localhost:3001/api/signup", {
                name,
                email,
                password,
            });

            dispatch(loginSuccess({ user: res.data.user, token: res.data.access_token }));
            localStorage.setItem("token", res.data.access_token);
            navigate("/home");
        } catch (err) {
            console.error(err);
            setError(err.response?.data?.error || "Error al registrarse");
        }
    };

    return (
        <div className="w-full max-w-md p-6 bg-white rounded-xl shadow-md">
            <h2 className="text-2xl font-semibold text-center text-gray-800 mb-6">Registro</h2>

            <form onSubmit={handleSignUp} className="space-y-4">
                <div>
                    <input
                        type="text"
                        placeholder="Nombre"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <input
                        type="email"
                        placeholder="Correo electrónico"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <input
                        type="password"
                        placeholder="Contraseña"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <button
                    type="submit"
                    className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition-colors"
                >
                    Registrar
                </button>
            </form>

            {error && (
                <p className="text-red-500 text-sm text-center mt-4">
                    {error}
                </p>
            )}
        </div>
    );
};
