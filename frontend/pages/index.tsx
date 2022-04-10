import { useEffect, useState, useCallback } from 'react'

import type { NextPage } from 'next'
import Head from 'next/head'
import styles from '../styles/Home.module.css'
import PennSched from '../components/pennsched'

const Home: NextPage = () => {
  return (
    <div className={styles.container}>
      <Head>
        <title>PennSched</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <PennSched />
      </main>
    </div>
  )
}

export default Home
