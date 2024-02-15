import Link from 'next/link';
import classes from './Layout.module.scss';
import Image from 'next/image';

import logo from '../../assets/images/logo.png';

import { ICategory } from '@/utils/interfaces';
import SearchForm from './SearchForm';

async function fetchCategories(): Promise<ICategory[]> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/categories/parent`,
    { cache: 'no-store' }
  );
  return response.json();
}

async function fetchProductCount(): Promise<{ count: number }> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/products/count`,
    { cache: 'no-store' }
  );

  return response.json();
}

async function Nav() {
  const [categories, productCount] = await Promise.all([
    fetchCategories(),
    fetchProductCount(),
  ]);

  return (
    <nav className={classes.navigation}>
      <div className={classes.wrapper}>
        <div className={classes.logo}>
          <Link href='/' legacyBehavior={true}>
            <Image src={logo} alt='Zenith tech' />
          </Link>
        </div>
        <SearchForm productCount={productCount.count} />
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
