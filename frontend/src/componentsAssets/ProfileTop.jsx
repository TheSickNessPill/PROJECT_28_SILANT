import React from "react";
import { Link } from "react-router-dom";

import "./../style/ProfileTop.css";

export default function ProfileTop() {
    const localStorage = window.localStorage;
    const companyName = localStorage.getItem("companyName") || "";
    const role = localStorage.getItem("role");

    return (
        <div className="profile-top-container">
            <p> Приветствую, </p>
            <p> {companyName || role} </p>
            <Link to="/logout"> Выйти </Link>
        </div>
    )
}