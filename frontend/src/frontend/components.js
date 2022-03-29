import React, {useEffect, useState}  from 'react'
import { loadUploads } from '../lookup'

export function UploadsList(props){
    const [uploads, setUploads] = useState([])
   
    useEffect(() => {
      const myCallback = (response, status) => {
        if (status === 200){
          setUploads(response)
        } else {
          alert("There was an error")
        }
      }
      loadUploads(myCallback)
    }, [])
    return uploads.map((item, index)=>{
      return <Uploads upload={item} className='my-5 py-5 border bg-white text-dark' key={`${index}-{item.id}`} />
    })
}


export function Uploads(props) {
    const {upload} = props
    const className = props.className ? props.className : 'col-10 mx-auto col-md-6'
    return <div className={className}>
        <p>{upload.id}</p>
        <img src={upload.file}  alt="user-photos"/>
    </div>
  }
  