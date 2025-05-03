import React from "react";
import { LoginFormComponent } from '../components/LoginFormComponent.jsx';


export const Login = () => {
    return (
        <div className="container h-screen text-center my-5">
            <div className="title-box">
                <h1>Login!</h1>
                <LoginFormComponent />
            </div>
        </div>
    )
}