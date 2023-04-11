import { useState } from 'react'
import './App.css'
import Glass from './components/Glass'

function App() {
  const [count, setCount] = useState(0)

  return (

    <section>
        <div class="color"></div>
        <div class="color"></div>
        <div class="color"></div>
        <div className="box">
          <div className="square" style={{ '--i': 0 }}></div>
          <div className="square" style={{ '--i': 1 }}></div>
          <div className="square" style={{ '--i': 2 }}></div>
          <div className="square" style={{ '--i': 3 }}></div>
          <div className="square" style={{ '--i': 4 }}></div>
          <div class="container">
            <Glass/>
          </div>
        </div>
    </section>
  )
}

export default App
