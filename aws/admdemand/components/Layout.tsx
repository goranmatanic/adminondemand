import React, { ReactNode } from 'react'
import Link from 'next/link'
import Head from 'next/head'

type Props = {
  children?: ReactNode
  title?: string
}

const Layout = ({ children, title = 'This is the default title' }: Props) => (
  <div className="min-h-screen flex flex-col">
    <Head>
      <title>{title}</title>
      <meta charSet="utf-8" />
      <meta name="viewport" content="initial-scale=1.0, width=device-width" />
    </Head>
    <header className="bg-gray-300 p-4 flex justify-between items-center">
      <nav>
        <Link className="text-xl font-bold hover:text-blue-500" href="/">Home</Link>
      </nav>
    </header>
    <main className="flex-1 p-4">{children}</main>
  </div>
)

export default Layout