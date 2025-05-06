// frontend/components/GoogleLoginButton.jsx
import { GoogleLogin } from '@react-oauth/google';
import { useDispatch } from 'react-redux';
import { loginSuccess } from '../features/auth/slices/authSlice.js';
import { useNavigate } from 'react-router-dom';

export const GoogleLoginButton = () => {
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleSuccess = async (credentialResponse) => {
        const tokenId = credentialResponse.credential;

        try {
            const res = await fetch("http://localhost:3001/api/auth/google", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ token: tokenId }),
            });

            const data = await res.json();

            if (res.ok) {
                dispatch(loginSuccess({ user: data.user, token: data.access_token }));
                localStorage.setItem("token", data.access_token);
                navigate("/home");
            } else {
                console.error("Error del servidor:", data.error);
            }
        } catch (err) {
            console.error("Error al conectar con el backend", err);
        }
    };

    return (
        <div className='my-5'>
            <GoogleLogin
                onSuccess={handleSuccess}
                onError={() => console.log("Error en el login con Google")}
            />
        </div>
    );
};
