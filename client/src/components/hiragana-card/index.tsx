type Props = {
  kana: string;
  romaji: string;
  image?: string;
}

const HiraganaCard = (props: Props) => {

  const { kana, romaji } = props;

  return (
    <a className="flex flex-col group bg-white border shadow-sm rounded-xl overflow-hidden hover:shadow-lg focus:outline-none focus:shadow-lg transition" href="#">
  <div className="relative pt-[50%] sm:pt-[60%] lg:pt-[80%] rounded-t-xl overflow-hidden">
    <img className="size-full absolute top-0 start-0 object-cover group-hover:scale-105 group-focus:scale-105 transition-transform duration-500 ease-in-out rounded-t-xl" src="https://images.unsplash.com/photo-1680868543815-b8666dba60f7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=560&q=80" alt="Card Image" />
  </div>
  <div className="p-4 md:p-5">
    <h3 className="text-lg font-bold text-gray-800 ">
      {kana} - {romaji}
    </h3>
    <p className="mt-1 text-gray-500">
      
    </p>
  </div>
</a>
  )
}

export default HiraganaCard