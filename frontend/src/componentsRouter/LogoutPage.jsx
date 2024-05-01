import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router";
import { useQuery } from "@tanstack/react-query";

import { apiSilantLogout } from "../api/apiAuth.js";

export default function LogoutPage() {
    const navigate = useNavigate();

    const token = window.localStorage.getItem("token") || "";

    const apiSilantLogoutResponse = useQuery({
        queryFn: () => apiSilantLogout(token),
        queryKey: ["apiSilantLogoutResponse"],
        enabled: token.length ? true : false
    })

    useEffect(
        () => {
            console.log("apiSilantLogoutResponse.isFetched", apiSilantLogoutResponse.isFetched)
            window.localStorage.clear();
            navigate("/");
            console.log("session cleared");
        },
        [apiSilantLogoutResponse.isFetched]
    );
    return (<p>Выход</p>);
};