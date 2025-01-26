import './styles/App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Navbar } from './components/Navbar.jsx'
import { Home } from './pages/Home.jsx'
import { About } from './pages/About.jsx'
import { Login } from './pages/Login.jsx'
import { Footer } from './components/Footer.jsx'
import { Signup } from './pages/Signup.jsx'


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
