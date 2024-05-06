import React, { useState, useEffect } from 'react';

function Home() {
    const [projects, setProjects] = useState([])

    useEffect(() => {
        fetch("http://127.0.0.1:5555/projects")
            .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
            })
            .then((data) => {
                console.log(data);
                setProjects(data);
            })
            .catch((error) => console.error("Fetch error:", error));
        }, []);
    
        const renderProjects = projects.map((project) => <ProjectCard key={project.id} project={project}/>)

        return (
            <>
            <main>
                {renderProjects}
            </main>
            </>
        )
}

export default Home