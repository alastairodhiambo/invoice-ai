import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import { Bar } from 'react-chartjs-2';
import { Chart as ChartJS,
         BarElement,
         CategoryScale,
         LinearScale, 
         Tooltip,
         Legend
       } from 'chart.js'

const inter = Inter({ subsets: ['latin'] })

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
)


export default function Home() {
  const data = {
    labels: ['Mon', 'Tue', 'Wed'],
    datasets: [
      { 
        label: '396',
        data: [3, 6, 9],
        backgroundColor: 'aqua',
        borderColor: 'black',
        borderWidth: 1,
      }
    ]
  }

  const options = {

  }

  return (
    <div style={{display: "flex", flexDirection: 'column'}}>
      <h1 style={{fontFamily:"Lucida Console", marginTop: "10vh", marginLeft: "10vw"}}>
        Hello, Welcome to Invoice AI
      </h1>
      <input style={{marginTop: '5vh', marginLeft: "10vw", borderRadius: "3px", width: "80%", height: "5vh", fontSize: "1.5rem", paddingLeft: "1%", color: "grey"}}/>
      <text style={{marginLeft: "10%", marginTop: "4vh", width: "80%"}}>Hello, The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.The quick brown fox jumps over the lazy dog.</text>
      <button style={{width: "10%", marginLeft: "10%", marginTop: "2%", marginBottom: "2%"}}>Submit</button>
      <Bar
        data={data}
        options={options}
      ></Bar>
    </div>
  )
}
