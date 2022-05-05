import React from 'react'
import { useNavigate, } from 'react-router-dom'
import Helmet from 'react-helmet'

export default function HomeComponent() {
  const navigate = useNavigate()
  
  return (
    <>
      <Helmet>
        <title>Django Boilerplate</title>
      </Helmet>
      <div className='container'>
        <div className="col-md-6 offset-md-3 text-center">
          <h1>Test</h1>
          <button className='btn btn-primary'>
            Test button
          </button>
        </div>
      </div>
    </>       
  )
}
