import './frontend/styles/App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Navbar } from './frontend/components/Navbar.jsx'
import { Home } from './frontend/pages/Home.jsx'
import { About } from './frontend/pages/About.jsx'
import { Login } from './frontend/pages/Login.jsx'
import { Footer } from './frontend/components/Footer.jsx'
import { Signup } from './frontend/pages/Signup.jsx'


function App() {

    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path='/' element={<Home />}></Route>
                <Route path='/home' element={<Home />}></Route>
                <Route path='/about' element={<About />}></Route>
                <Route path='/login' element={<Login />}></Route>
                <Route path='/signup' element={<Signup />}></Route>
            </Routes>
            <Footer />
        </BrowserRouter>
    )
}

export default App
