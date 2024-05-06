import React from "react";
import { NavLink } from "react-router-dom";
import "./NavBar.css";

function NavBar() {
    return (
        <>
        <nav className="navbar">
            <NavLink to='/home'>Home</NavLink>
            <NavLink to='/contact'>Contact</NavLink>
        </nav>
        </>
    )
}

export default NavBar