import { useState, useEffect } from 'react'

function Project({project}) {

    return (
        <>
            <div className='post-cards'>
                <p>Name: {project.name}</p>
                <p>Description: {project.description}</p>
                <p>Technology Stack: {project.stack}</p>
                <p>Github: {project.link}</p>
                <p>Demo: {project.demo}</p>
            </div>
        </>
    )

}

export default Project