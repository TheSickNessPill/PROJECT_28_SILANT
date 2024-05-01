import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router";
import Login from "./Login.jsx";
import ProfileTop from "./ProfileTop.jsx";

import "./../style/Session.css";

export default function Session() {
    const navigate = useNavigate();

    const localStorage = window.localStorage;
    const token = localStorage.getItem("token");
    const expiredDateTimeString = window.localStorage.getItem("expiredTime");

    useEffect(
        () => {
            if (!expiredDateTimeString) { return undefined; }
            const expiredDateTimeTimestamp = new Date(expiredDateTimeString).getTime();
            const nowUTCDateTime = new Date().getTime() - new Date().getTimezoneOffset() * 60;
            const nowUTCTimeStamp = new Date(nowUTCDateTime).getTime()

            if (expiredDateTimeTimestamp < nowUTCTimeStamp) {
                navigate("/logout");
            }
        }, []
    )

    return (
        <div className="top-profile-session">
            {
                token ? <ProfileTop /> : <Login />
            }
        </div>
    );
};