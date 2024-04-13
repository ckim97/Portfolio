import React from "react";
import App from "./components/App.jsx";
import Home from "./components/Home.jsx";
import Contact from "./components/Contact.jsx"

const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <h1>Something went wrong!</h1>,
        children: [
            {
                path: "/home",
                element: <Home/>,
                errorElement: <h1>Something went wrong!</h1>
            },
            {
                path: "/contact",
                element: <Contact />,
                errorElement: <h1>Something went wrong!</h1>
            }
        ]
    }
]

export default routes;