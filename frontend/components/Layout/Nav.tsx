import Link from 'next/link';
import classes from './Layout.module.scss';
import Image from 'next/image';

import { IoSearch } from 'react-icons/io5';

import logo from '../../assets/images/logo.png';

function Nav() {
  return (
    <nav className={classes.navigation}>
      <div className={classes.logo}>
        <Link href='/' legacyBehavior={true}>
          <Image src={logo} alt='Zenith tech' />
        </Link>
      </div>
      <form className={classes.inputWrapper}>
        <input type='text' placeholder='Search over 5000 products...' />
        <button type='submit'>
          <span>
            <IoSearch />
          </span>
        </button>
      </form>
      <div className={classes.actions}>
        <Link href='/contact' legacyBehavior>
          <a className='btn btn-primary'>
            <span>Login</span>
          </a>
        </Link>
      </div>
    </nav>
  );
}

export default Nav;
