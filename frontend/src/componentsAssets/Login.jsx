import React from "react";
import { Link } from "react-router-dom";

import "./../style/Login.css";

export default function Login(){

    return (
        <div className="login-container">
            <Link to="/login"> Авторизоваться </Link>
        </div>
    );
};