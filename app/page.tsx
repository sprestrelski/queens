import type { Metadata } from "next";
import Grid from "./components/Grid";

export default function IndexPage() {
  const formatDate = (date: Date): string => {
    const month = String(date.getMonth() + 1).padStart(2, "0");
    const day = String(date.getDate()).padStart(2, "0");
    const year = date.getFullYear();
    return `${month}_${day}_${year}`;
  };

  const todayDate = formatDate(new Date());

  return (
    <>
      <h1>today's puzzle</h1>
      <div>
        <Grid date={todayDate}/>
      </div>
    </>
  );
}

export const metadata: Metadata = {
  title: "queens archive",
};
