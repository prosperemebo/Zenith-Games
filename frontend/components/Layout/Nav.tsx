import Link from 'next/link';
import classes from './Layout.module.scss';
import Image from 'next/image';

import { IoSearch } from 'react-icons/io5';

import logo from '../../assets/images/logo.png';
import { ICategory } from '@/utils/interfaces';

async function fetchCategories(): Promise<ICategory[]> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/categories/parent`,
    { cache: 'no-store' }
  );
  return response.json();
}

async function Nav() {
  const categories = await fetchCategories();

  return (
    <nav className={classes.navigation}>
      <div className={classes.wrapper}>
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
          <Link href='/' legacyBehavior>
            <a className='btn btn-primary'>
              <span>Login</span>
            </a>
          </Link>
        </div>
      </div>
      <ul className={classes.menu}>
        {categories?.map((category) => (
          <li key={category.id}>
            <Link href={`/categories/${category.slug}`} legacyBehavior>
              <a dangerouslySetInnerHTML={{ __html: category.label }}></a>
            </Link>
          </li>
        ))}
      </ul>
    </nav>
  );
}

export default Nav;
