type Props = {
  card: {
    kana: string,
    romanji: string,
    audio?: string,
    image?: string,
    drawing?: string
  }
}

const DrawingPage = (props: Props) => {
  return (
    <div>
      <h1>{props.card.kana}</h1>
      <p>{props.card.romanji}</p>
    </div>
  )
}

export default DrawingPage