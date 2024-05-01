import React from "react";
import { useNavigate } from "react-router-dom";
import { useEffect, useState, useMemo } from "react";
import { useSelector } from "react-redux";

import "./../style/SilantTable.css";

export default function SilantTable(props) {
    const navigate = useNavigate();
    const header = props.header;
    const data = props.data;
    const identifiers = props.identifiers;
    const tableName = props.tableName;

    const detailedDataEndpoint = tableName === "mashine" ?
        "/detailMashineData/"
        :
        tableName === "serviceCenter" ?
            "/detailMashineData/"
            :
            tableName === "complaints" ?
                "/detailComplaintsData/"
                :
                "";


    const [filter, setFilter] = useState("");
    const [sortConfig, setSortConfig] = useState({ key: null, direction: "ascending" });

    //sort
    const sortedData = useMemo(
        () => {
            const sortableItems = data;
            if (sortConfig.key !== null) {
                sortableItems.sort(
                    (a, b) => {
                        if (a[sortConfig.key] < b[sortConfig.key]) {
                            return sortConfig.direction === 'ascending' ? -1 : 1;
                        }
                        if (a[sortConfig.key] > b[sortConfig.key]) {
                            return sortConfig.direction === 'ascending' ? 1 : -1;
                        }
                        return 0;
                    }
                );
            }
            // console.log("112233", sortableItems[0][0], data[0][0])
            // console.log("sort")
            return sortableItems;
        }, [data, sortConfig]
    );

    // filter
    const filteredData = useMemo(
        () => {
            return sortedData.filter(
                (row) => {
                    return row.some(
                        (value) => {
                            return value.toString().toLowerCase().includes(filter.toLowerCase());
                        }
                    );
                }
            );
        }, [sortedData[0], filter]
    );

    // sort processor
    function requestSort(key) {
        let direction = "ascending";
        if (sortConfig.key === key && sortConfig.direction === 'ascending') {
            direction = "descending";
        }
        setSortConfig({ key, direction });
    };


    return (
        <div className="silant-table-container">
            <div className="filter-input">
                <label htmlFor="filterName">Фильтр по любому значению: </label>
                <input
                    type="text"
                    value={filter}
                    name="filterName"
                    onChange={(e) => { setFilter(e.target.value); }}
                />
            </div>
            <div className="table-container">
                <table>
                    <thead>
                        <tr>
                            {
                                header.map(
                                    (headerElem, index) => {
                                        return <th
                                            key={headerElem}
                                            onClick={() => { requestSort(index) }}
                                        > {headerElem}
                                        </th>
                                    }
                                )
                            }
                        </tr>
                    </thead>
                    <tbody>
                        {
                            filteredData.map(
                                (row, rowIndex) => {
                                    return <tr onClick={() => { }} key={rowIndex}>
                                        {
                                            row.map(
                                                (cell, cellIndex) => {
                                                    return <td key={cellIndex}> {cell}</td>
                                                }
                                            )
                                        }
                                    </tr>
                                }
                            )
                        }
                    </tbody>
                </table>
            </div>
        </div>
    );
}