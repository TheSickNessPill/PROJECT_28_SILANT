import React from "react";
import { useState, useEffect, useMemo } from "react";
import { useQuery } from "@tanstack/react-query";

import { apiFullDataByUser } from "../api/apiMashines.js";

import Loading from "./Loading.jsx";
import SilantTable from "./SilantTable.jsx";

import "./../style/AuthMainPage.css";


export default function AuthMainPage() {
    const token = window.localStorage.getItem("token");
    const companyName = window.localStorage.getItem("companyName");
    const role = window.localStorage.getItem("role");

    const [currentHeaders, setCurrentHeaders] = useState([]);
    const [currentData, setCurrentData] = useState([]);
    const [currentTable, setCurrentTable] = useState("");
    const [currentIdentifiers, setCurrentIdentifiers] = useState([]);

    const fullDataByUserResponse = useQuery({
        queryFn: () => apiFullDataByUser(token, role),
        queryKey: ["fullDataByUserResponse"],
        staleTime: Infinity
    });

    if (fullDataByUserResponse.isLoading) { return <Loading /> }
    return (
        <main className="auth-main-page">
            <div className="client-name-container">
                <h1>
                    {
                        role === "client" ?
                            "Клиент" :
                            role === "service_company" ?
                                "Сервисная компания" :
                                role === "manager" ?
                                    "Мэнэджер" :
                                    ""
                    } {companyName? `: ${companyName}` : undefined}
                </h1>
            </div>
            <div className="tables-description">
                <p> Информация о комплектайии и технических характеристик Вашей техники </p>
            </div>
            <div className="tables-container">
                <div className="tables-nav">
                    <button
                        onClick={()=>{
                        setCurrentHeaders(fullDataByUserResponse.data.mashineFieldsName);
                        setCurrentData(fullDataByUserResponse.data.mashinesData);
                        setCurrentIdentifiers(fullDataByUserResponse.data.mashinesDataIds);
                        setCurrentTable("mashine");
                    }}> Машины </button>
                    <button onClick={()=>{
                        setCurrentHeaders(fullDataByUserResponse.data.maintanceFieldsName);
                        setCurrentData(fullDataByUserResponse.data.maintanceData);
                        setCurrentIdentifiers(fullDataByUserResponse.data.maintanceDataIds);
                        setCurrentTable("serviceCenter");
                    }}> ТО </button>
                    <button onClick={()=>{
                        setCurrentHeaders(fullDataByUserResponse.data.complaintsFieldsName);
                        setCurrentData(fullDataByUserResponse.data.complaintsData);
                        setCurrentIdentifiers(fullDataByUserResponse.data.complaintsDataIds);
                        setCurrentTable("complaints");
                    }}> Рекламации </button>
                </div>
                {
                    currentHeaders.length && currentData.length ?
                        <SilantTable
                            header={currentHeaders}
                            data={currentData}
                            tableName={currentTable}
                            identifiers={currentIdentifiers}
                        />
                        :
                        undefined
                }
            </div>
        </main>
    );
}