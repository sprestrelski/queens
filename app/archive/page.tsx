import Grid from "../components/Grid";

export default function ArchivePage() {
  const dates = ["05_27_2024", "05_26_2024", "05_25_2024", "05_24_2024", "05_23_2024"]

  return (
    <>

      {dates.map((date, index) => {
        const formattedDate = date.replace(/_/g, '/');
        return (
        <div key={index}>
          <h2>{formattedDate}</h2>
          <Grid date={date} />
        </div>
        );
      })}
    </>
  );
}
