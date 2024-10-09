import HiraganaCard from "./components/hiragana-card";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/home";
import LoginPage from "./pages/login";
import { ProtectedRoutes } from "./components/protected-route/page";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route element={<ProtectedRoutes />}>
          <Route path="/" element={<Home />} />
          {/* <Route path="/:id" element={<HiraganaCard />} /> */}
        </Route>
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </Router>
  );
}
