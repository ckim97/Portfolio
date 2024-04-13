import React from "react";
import { NavLink } from "react-router-dom";

function NavBar() {
    return (
        <>
        <nav>
            <NavLink to='/home'>Home</NavLink>
            <NavLink to='/contact'>Contact</NavLink>
        </nav>
        </>
    )
}

export default NavBar