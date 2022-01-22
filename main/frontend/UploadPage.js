import React, { useState } from 'react'
import ReactDOM from 'react-dom'
import Cropper from 'react-easy-crop'


const App = () => {
  const [crop, setCrop] = useState({ x: 0, y: 0 })
  const [zoom, setZoom] = useState(1)

  let [] = useState([])
  return (
    <div className="App">
      <div className="crop-container">
        <Cropper
          video="https://vid.ly/5u4h3e?content=video"
          crop={crop}
          zoom={zoom}
          aspect={4 / 3}
          onCropChange={setCrop}
          onZoomChange={setZoom}
          onImageLoaded={res => {
            console.log(res)
          }}
        />
      </div>
      <div className="controls" />
    </div>
  )
}

const rootElement = document.getElementById('root')
ReactDOM.render(<App />, rootElement)
export default App
