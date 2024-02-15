import type { Metadata } from 'next';
import Nav from '../../../components/Layout/Nav';

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div className='body-wrapper'>
      <Nav />
      {children}
    </div>
  );
}
