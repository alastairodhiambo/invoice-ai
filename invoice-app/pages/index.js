import { useState } from "react";
import { Inter } from "next/font/google";
import { AwesomeButton } from "react-awesome-button";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

import "react-awesome-button/dist/styles.css";

import { UserData } from "../pages/UserData";

ChartJS.register(BarElement, CategoryScale, LinearScale, Tooltip, Legend);

//uvicorn main:app --reload

export default function Home() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [query, setQuery] = useState("");

  const data = {
    labels: UserData.map((o) => o.year),
    datasets: [
      {
        label: "Year Total",
        backgroundColor: "#339af0",
        borderColor: "rgb(0, 255, 0)",
        borderWidth: 1,
        data: UserData.map((o) => o.userGain),
      },
    ],
  };

  const options = {
    plugins: {
      title: {
        display: true,
        text: "Bar Chart",
      },
    },
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (selectedFile) {
      const formData = new FormData();
      formData.append("file", selectedFile);

      try {
        const response = await fetch("http://127.0.0.1:8000/uploadfile/", {
          method: "POST",
          body: formData,
        });

        if (response.ok) {
          console.log("File uploaded successfully");
        } else {
          console.error("File upload failed");
        }
      } catch (error) {
        console.error(error);
      }
    }
  };

  const handleQuery = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:8000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: query }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log(data);
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleInputChange = (event) => {
    setQuery(event.target.value);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column" }}>
      <h1
        style={{
          fontFamily: "Lucida Console",
          marginTop: "10vh",
          marginLeft: "10vw",
        }}
      >
        Hello, Welcome to Invoice AI
      </h1>

      <input
        style={{
          marginTop: "5vh",
          marginLeft: "10vw",
          borderRadius: "3px",
          width: "80%",
          height: "5vh",
          fontSize: "1.5rem",
          paddingLeft: "1%",
          color: "grey",
        }}
        type="text"
        name="query"
        onChange={handleInputChange}
      />
      <AwesomeButton
        onPress={handleQuery}
        style={{ width: "10%", marginLeft: "10%", marginTop: "1%" }}
        type="primary"
      >
        Submit
      </AwesomeButton>

      <form onSubmit={handleSubmit} style={{ marginTop: "2%" }}>
        <AwesomeButton
          style={{ width: "10%", marginLeft: "10%", marginRight: "2%" }}
          type="primary"
        >
          Upload
        </AwesomeButton>
        <input type="file" onChange={handleFileChange} />
      </form>
      <div style={{ width: "50%", marginLeft: "25%" }}>
        <Bar data={data} options={options}></Bar>
      </div>
    </div>
  );
}
