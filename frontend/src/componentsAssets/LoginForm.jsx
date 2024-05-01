import React from "react";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router";
import { useQuery } from "@tanstack/react-query";

import { apiSilantlogin } from "../api/apiAuth.js";

import "./../style/LoginForm.css";

export default function LoginForm() {
    const navigate = useNavigate();
    const [login, setLogin] = useState("");
    const [password, setPassword] = useState("");
    const [authButtonDisabledFlag, setAuthButtonDisabledFlag] = useState(true);
    const [errorText, setErrorText] = useState("");

    const silantLoginResponse = useQuery({
        queryFn: () => apiSilantlogin(login, password),
        queryKey: ["silantlogin"],
        enabled: false,
        staleTime: Infinity
    });

    useEffect(
        ()=>{
            if (window.localStorage.getItem("token")){
                navigate("/");
            }
        },
        []
    );

    useEffect(
        ()=>{
            if (silantLoginResponse.isFetched){

                setErrorText("");
                if (silantLoginResponse.data.status === "ok"){
                    const localStorage = window.localStorage;
                    console.log(silantLoginResponse.data.access)
                    localStorage.setItem("companyName", silantLoginResponse.data.companyName || "");
                    localStorage.setItem("role", silantLoginResponse.data.role);
                    localStorage.setItem("access", JSON.stringify(silantLoginResponse.data.access));
                    localStorage.setItem("token", silantLoginResponse.data.token);
                    localStorage.setItem("expiredTime", silantLoginResponse.data.expired_time);
                    setAuthButtonDisabledFlag(true);
                    navigate("/");
                }
                else if (silantLoginResponse.data.status === "error"){
                    console.log(silantLoginResponse.data.text)
                    setErrorText(silantLoginResponse.data.text);
                }
                // console.log("res", silantLoginResponse.data )
            }
        },
        [silantLoginResponse.dataUpdatedAt]
    )

    useEffect(
        () => {
            if (login.length > 3 && password.length > 3) {
                setAuthButtonDisabledFlag(false);
            }
            else {
                setAuthButtonDisabledFlag(true);
            }
        },
        [login, password]
    );

    function getAuth() {
        // console.log(login, password);
        console.log("Login");
        silantLoginResponse.refetch();
    }

    return (
        <div className="login-form-wrapper">
            <div className="login-form-container">
                <form className="login-form">
                    <fieldset>
                        <div>
                            <label htmlFor="login"> Логин:  </label>
                            <input type="text" name="login" onChange={(e) => { setLogin(e.target.value.trim()); }} />
                        </div>
                        <div>
                            <label htmlFor="password"> Пароль: </label>
                            <input type="password" name="password" onChange={(e) => { setPassword(e.target.value.trim()); }} />
                        </div>
                    </fieldset>
                </form>
            </div>
            <div className="login-button-container">
                <button disabled={authButtonDisabledFlag} onClick={() => { getAuth() }} > Авторизоваться </button>
            </div>
            <div className="auth-error-text-container">
                <p>{errorText}</p>
            </div>
        </div>
    );
};