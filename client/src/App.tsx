import CardContainer from "./components/card-container";
import HiraganaCard from "./components/hiragana-card";
import Navbar from "./components/navbar";

export default function App() {
  return (
    <>
    <Navbar />
    <main className="max-w-screen-xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
      <h1 className="text-3xl font-bold text-gray-900">Hiragana</h1>
      <p className="mt-1.5 text-sm text-gray-500">
        Click on a card to start learning!
      </p>
      <CardContainer />
    </main>
    </>
  )
}