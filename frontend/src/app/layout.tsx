import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import '../sass/main.scss';
import Nav from '../../components/Layout/Nav';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Zenith Tech',
  description:
    'Hottest hub for tech enthausists. Get your games and gadgets at the best prices!',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang='en'>
      <head>
      </head>
      <body className={inter.className}>
        <div className='body-wrapper'>
          <Nav />
          {children}
        </div>
      </body>
    </html>
  );
}
