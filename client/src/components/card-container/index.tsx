import axios from "axios";
import { useEffect, useState } from "react";
import DrawingCanvas from "../drawing-canvas";
import styled from "styled-components";
import useLocalStorage from "../../hooks/useLocalStorage";
import { MakeRequest } from "../../utils/axiosWrapper";

const GlassButton = styled.button`
    width: 70%;
    margin: 40px auto;
    padding: 2rem;
    background: rgba(0, 166, 255, 0.3);
    color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    padding: 2rem;
  `;

const CardContainer = () => {
  type Card = {
    id: number;
    kana: string;
    romaji: string;
  };

  const [cards, setCards] = useState<Card[]>([]);
  const [drawWindowOpen, setDrawWindowOpen] = useState(false);
  const [card, setCard] = useState<Card>();

  const [count, setCount] = useLocalStorage("count", 0);

  useEffect(() => {
    if (card) {
      setDrawWindowOpen(true);
    } else {
      setDrawWindowOpen(false);
    }
  }, [card]);

  const handleClose = (cardId: number) => {
    setDrawWindowOpen(false);
    const updateUserProgress = async () => {
      try {
        const response = await MakeRequest({
          method: "PUT",
          route: `/cards/progress/${cardId}`,
          data: {"last_reviewed_at": new Date()}
        });
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    };
    if (cardId) {
      updateUserProgress();
    }
  };

  const handleClick = (selectedCard: Card) => {
    console.log("card data", selectedCard);
    setCard(selectedCard);
  };

  useEffect(() => {
    const fetchCards = async () => {
      const response = await MakeRequest({
        method: "GET",
        route: "/cards",
      });
      setCards(response);
    };
    fetchCards();
  }, []);

  

  return (
    <div className="grid grid-cols-5 gap-1">
      {drawWindowOpen && card && (
        <DrawingCanvas card={card} closeModal={() => handleClose(card.id)} />
      )}
      {cards ? (
        cards.map((card, index) => (
          <GlassButton onClick={() => handleClick(card)} key={index}>
            <h3 key={index}>{card.kana}</h3>
            <p>{card.romaji}</p>
          </GlassButton>
        ))
      ) : (
        <p>No cards to display</p>
      )}
    </div>
  );
};

export default CardContainer;
