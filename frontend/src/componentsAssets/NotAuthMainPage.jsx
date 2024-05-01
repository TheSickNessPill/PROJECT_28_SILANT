import React from "react";
import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useQuery } from "@tanstack/react-query";

import { apiBaseMashines } from "../api/apiMashines.js";

import Loading from "./Loading.jsx";
import SilantTable from "./SilantTable.jsx";

import "./../style/NotAuthMainPage.css";

export default function NotAuthMainPage(){
    const [factoryNumber, setFartoryNumber] = useState("");
    const [baseMashinesRequestFlag, setBaseMashinesRequestFlag] = useState(false);


    const baseMashinesRequest = useQuery({
        queryFn: () => apiBaseMashines(factoryNumber),
        queryKey: ["baseMashinesRequest"],
        staleTime: Infinity,
        enabled: baseMashinesRequestFlag
    });

    function processFindButton(){
        if (!baseMashinesRequestFlag){setBaseMashinesRequestFlag(true);}
        else {baseMashinesRequest.refetch();}
    }

    return (
        <main className="not-auth-main-page">
            <h1> Првоерьте комплектацию и технические характеристики техники Силант</h1>
            <div className="search-container">
                <div>
                    <label htmlFor="factoryNumber"> Зав. номер: </label>
                    <input
                        type="text"
                        name="factoryNumber"
                        onChange={(e)=>{setFartoryNumber(e.target.value);}}
                    />
                </div>
                <div className="search-button">
                    <button
                        disabled={factoryNumber.length? false: true}
                        onClick={() => processFindButton()}
                    > Поиск </button>
                </div>
            </div>
            <div className="result-description">
                <p> Результат поиска: </p>
                <p> Информация о комплектации и технических характеристик Вашей техники. </p>
            </div>
            <div className="base-table-data-container">
                {
                    baseMashinesRequest.isLoading ?
                        <Loading />
                        :
                        baseMashinesRequest.isFetched ?
                            baseMashinesRequest.data.status === "ok"?
                                <SilantTable
                                    header={baseMashinesRequest.data.header}
                                    data={baseMashinesRequest.data.baseMashineData}
                                />
                                :
                                <p className="no-data-warning"> {baseMashinesRequest.data.text} </p>
                            :
                            undefined
                }
            </div>
        </main>
    );
}