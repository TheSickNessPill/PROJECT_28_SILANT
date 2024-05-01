import React from "react";

import logo_blue from "./../media/Logotype_blue.jpg";
import logo_red from "./../media/Logotype_red.jpg";
import logo_white from "./../media/Logotype_white.jpg";

import "./../style/Logo.css";

export default function Logo(props) {
    const color = props.color || "blue";

    return (
        <div className="silant-logo">
            <img
                src={
                    color === "blue" ?
                        logo_blue :
                        color === "red" ?
                            logo_red :
                            color === "white" ?
                                logo_white :
                                logo_blue
                } />
        </div>
    );
};