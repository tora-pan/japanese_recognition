import Navbar from "./components/navbar/Navbar";

export default function App() {
  return (
    <>
    <Navbar />
    <main className="max-w-screen-xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
      <h1 className="text-3xl font-bold text-gray-900">Blog Posts</h1>
      <p className="mt-1.5 text-sm text-gray-500">
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Iure, recusandae.
      </p>
    </main>
    </>
  )
}