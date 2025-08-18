import React from 'react'

const Footer = () => {
  return (
    <>
      <footer className='footer py-3 my-3'>
        <hr className='border-bottom'/>
        <p className='text-light text-center'>
          &copy; {new Date().getFullYear()} - Built with ❤️ by Rakesh Joshi
        </p>
      </footer>
    </>
  )
}

export default Footer