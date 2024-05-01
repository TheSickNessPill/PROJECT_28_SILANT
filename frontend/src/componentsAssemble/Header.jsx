import React from "react";

import Logo from "../componentsAssets/Logo.jsx";
import CommunicationContacts from "../componentsAssets/CommunicationContacts.jsx";
import Session from "../componentsAssets/Session.jsx";
import HeaderTitle from "../componentsAssets/HeaderTitle.jsx";

import "./../style/Header.css";

export default function Header() {


    return (
        <header>
            <Logo color="blue" />
            <div>
                <CommunicationContacts />
                <HeaderTitle />
            </div>
            <Session />
        </header>
    );
};