import { Routes, Route } from 'react-router-dom'
import { Home } from '../pages/Home.jsx'
import { About } from '../pages/About.jsx'
import { Login } from '../features/auth/pages/Login.jsx'
import { Signup } from '../features/auth/pages/Signup.jsx'

export const AppRoutes = () => {
    return (
        <Routes>
            <Route path='/' element={<Home />}></Route>
            <Route path='/home' element={<Home />}></Route>
            <Route path='/about' element={<About />}></Route>
            <Route path='/login' element={<Login />}></Route>
            <Route path='/signup' element={<Signup />}></Route>
        </Routes>
    )
}