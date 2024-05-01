import React from "react";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Provider } from "react-redux";

import { store } from "../state/store.js";


import MainPage from "../componentsRouter/MainPage.jsx";
import LoginPage from "../componentsRouter/LoginPage.jsx";
import LogoutPage from "../componentsRouter/LogoutPage.jsx";


const queryClient = new QueryClient();
const router = createBrowserRouter([
    {
        path: "/",
        element: <MainPage />
    },
    {
        path: "/login",
        element: <LoginPage />
    },
    {
        path: "/logout",
        element: <LogoutPage />
    }
]);

export default function App() {

    return (
        <QueryClientProvider client={queryClient}>
            <Provider store={store}>
                <RouterProvider router={router}/>
            </Provider>
        </QueryClientProvider>
    );
};