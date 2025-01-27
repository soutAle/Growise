import React from "react";
import { CounterTest } from "../components/CounterTest.jsx";


export const Home = () => {
    return (
        <div className="container h-screen text-center my-5">
            <div className="title-box">
                <h1>Home</h1>
                <CounterTest />
            </div>
        </div>
    )
}