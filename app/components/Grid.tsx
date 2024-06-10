"use client";
import React, { useEffect, useState } from "react";
import styles from "./Grid.module.css"


const Grid = ({ date }: { date: string }) => {
  const [gridData, setGridData] = useState<number[]>([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch(`/_grids/${date}.json`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch, grid likely hasn't been uploaded yet");
        }
        return response.json();
      }
      )
      .then((data) => setGridData(data.gridData))
      .catch((error) => {
        setError(true);
        console.error("Error fetching grid data:", error)}
      );
  }, [date]);

  const [cellStates, setCellStates] = useState<(null | "X" | "Q")[]>([]);
  const cols = Math.sqrt(gridData.length)

  useEffect(() => {
    setCellStates(new Array(gridData.length).fill(null));
  }, [gridData]);

  const handleCellClick = (cellIndex: number) => {
    const newCellStates = [...cellStates];
    switch (newCellStates[cellIndex]) {
      case null: 
        newCellStates[cellIndex] = "X";
        break;
      case "X":
        newCellStates[cellIndex] = "Q";
        break;
      case "Q":
        newCellStates[cellIndex] = null;
        break;
      default:
        break;
    }
    setCellStates(newCellStates);
  };

  return (
    <>
      {error ? (
        <p> {date}'s grid hasn't been uploaded yet! check back later </p>
      ) : (
        <div className={styles.grid} style={{"--cols":cols} as React.CSSProperties}>
          {gridData.map((color, index) => (
            <div
              key={index}
              className={`${styles.cell}`}
              style={{ backgroundColor: getColor(color) }}
              onClick={() => handleCellClick(index)}
            >
              {cellStates[index]}
            </div>
          ))}
        </div>
      ) }
    </>
  );
};

const getColor = (colorNumber: number): string => {
  switch (colorNumber) {
    case 0:
      return "mediumpurple";
    case 1:
      return "sandybrown";
    case 2:
      return "cornflowerblue";
    case 3:
      return "lightgreen";
    case 4:
      return "lavender";
    case 5:
      return "lightpink";
    case 6:
      return "cadetblue";
    case 7:
      return "coral";
    case 8:
      return "khaki";
    case 9:
      return "tan";
    case 10:
      return "aqua";
    case 11:
      return "violet";
    default:
      return "black";
  }
};

export default Grid;
