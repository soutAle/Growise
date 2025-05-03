import './frontend/styles/App.css'
import { BrowserRouter } from 'react-router-dom'
import { Navbar } from './frontend/components/Navbar.jsx'
import { Footer } from './frontend/components/Footer.jsx'
import { AppRoutes } from './frontend/routes/AppRoutes.jsx'


function App() {

    return (
        <BrowserRouter>
            <Navbar />
            <AppRoutes />
            <Footer />
        </BrowserRouter>
    )
}

export default App
