import CardContainer from "./components/card-container";
import HiraganaCard from "./components/hiragana-card";
import { BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Home from "./pages/home";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/:id" element={<HiraganaCard />} />
      </Routes>
    </Router>
    
  )
}