import { useState } from 'react'
import NavBar from '../NavBar'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <header>
      <NavBar/>
    </header>
    </>
  )
}

export default App
