import React from "react";
import { SignUpFormComponent } from '../components/SingUpFormComponent.jsx';


export const Signup = () => {
    return (
        <div className="h-screen text-center my-5">
            <h1>Signup!</h1>
            <SignUpFormComponent />
        </div>
    )
}