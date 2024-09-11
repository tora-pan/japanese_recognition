const Navbar = () => {
  return (
    <header className="static bg-gray-50 dark:bg-gray-800">
  <div className="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
    <div className="flex flex-col items-start gap-4 md:flex-row md:items-center md:justify-between">
      <div>
        <h1 className="text-2xl font-bold text-gray-500 dark:text-white sm:text-3xl">Let's Learn</h1>

        <p className="mt-1.5 text-sm text-gray-500 dark:text-gray-400">
          Get ready to learn hiraganas, katakana and kanji today!
        </p>
      </div>

      <div className="flex items-center gap-4">
        <button
          className="inline-block rounded bg-indigo-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-indigo-700 focus:outline-none focus:ring"
          type="button"
        >
          Start Learning 
        </button>
      </div>
    </div>
  </div>
</header>
  )
}

export default Navbar