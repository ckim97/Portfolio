import { useState, useEffect } from 'react'
import NavBar from '../NavBar'
import Project from './Project'



function App() {
  const [projects, setProjects] = useState([])

  useEffect(() => {
    fetch('http://127.0.0.1:5555/projects')
      .then(r => r.json())
      .then((data) => {
        console.log(data)
        setProjects(data)
        console.log(projects)
      })
  }, [])

  const renderProjects = projects.map((project) => <Project key={project.id} project={project}/>)


  return (
    <>
    <header>
      <NavBar className="navbar"/>
    </header>
    <body>
      {renderProjects}
    </body>
   
    </>
  )
}

export default App
