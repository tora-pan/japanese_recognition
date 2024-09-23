import axios from "axios";
import { useEffect, useState } from "react";
import DrawingCanvas from "../drawing-canvas";

const CardContainer = () => {
  type Card = {
    kana: string;
    romaji: string;
  };

  const [cards, setCards] = useState<Card[]>([]);
  const [drawWindowOpen, setDrawWindowOpen] = useState(false);
  const [card, setCard] = useState<Card>();

  useEffect(() => {
    if (card){
      console.log('card is ', card);
      setDrawWindowOpen(true);
    }
    else {
      setDrawWindowOpen(false);
    }
  }
  , [card]);

  const handleClose = () => {
    setDrawWindowOpen(false);
  }

  const handleClick = (selectedCard:Card) => {
    setCard(selectedCard);
    console.log("Card state", selectedCard);
    // setDrawWindowOpen(!drawWindowOpen);
  }

  useEffect(() => {
    const fetchCards = async () => {
      const response = await axios.get("http://localhost:8003/cards");
      console.log(response.data);
      setCards(response.data);
    };
    fetchCards();
  }, []);

  return (
    <div className="grid grid-cols-5 gap-1">
      {drawWindowOpen && card && <DrawingCanvas card={card} closeModal={handleClose}/>}
      {cards ? (
        cards.map((card, index) => (
          <button onClick={() => handleClick(card)} key={index} className="border-2 border-gray-200 text-gray-700 p-4 hover:border-gray-500 hover:font-medium hover:text-blue-900 hover:text-md">
            <h3 key={index}>{card.kana}</h3>
            <p>{card.romaji}</p>
          </button>
        ))
      ) : (
        <p>No cards to display</p>
      )}
    </div>
  );
};

export default CardContainer;
