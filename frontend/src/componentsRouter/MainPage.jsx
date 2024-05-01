import React from "react";

import Header from "../componentsAssemble/Header.jsx";
import Footer from "../componentsAssemble/Footer.jsx";
import NotAuthMainPage from "../componentsAssets/NotAuthMainPage.jsx";
import AuthMainPage from "../componentsAssets/AuthMainPage.jsx";

export default function MainPage(){
    const token = window.localStorage.getItem("token");
    return (
        <React.Fragment>
            <Header />
            {
                token ?
                    <AuthMainPage />
                    :
                    <NotAuthMainPage />
            }
            <Footer />
        </React.Fragment>
    );
};