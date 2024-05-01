import React from "react";

import CommunicationContacts from "../componentsAssets/CommunicationContacts.jsx";
import Signature from "../componentsAssets/Signature.jsx";

import "./../style/Footer.css";


export default function Footer(){
    return (
        <footer>
            <CommunicationContacts />
            <Signature />
        </footer>
    );
}