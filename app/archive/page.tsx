import Grid from "../components/Grid";
import fs from 'fs';
import path from 'path';

const gridsFolder = path.join(process.cwd(), 'public', '_grids');

export default function ArchivePage() {
  const getFilesInFolder = (folderPath: fs.PathLike) => {
    const files = fs.readdirSync(folderPath);
    return files
      .filter(file => path.extname(file).toLowerCase() === '.json')
      .map(file => path.parse(file).name);
  };

  const dates = getFilesInFolder(gridsFolder).reverse();

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
