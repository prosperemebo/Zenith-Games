import { IProduct } from '@/utils/interfaces';
import classes from './Search.module.scss';
import Image from 'next/image';
import Link from 'next/link';

interface Props {
  products: IProduct[];
}

const SearchCatalog = ({ products }: Props) => {
  return (
    <main className={classes.wrapper}>
      <h2 className='heading-primary'>Found {products.length} products!</h2>
      <ul className={classes.products}>
        {products.map((product, index) => (
          <li key={product.id}>
            <Image
              width='500'
              height='500'
              draggable='false'
              src={product.cover_image?.split('?')[0]}
              alt={product.label}
              priority={index < 5}
            />
            <div className={classes.info}>
              <h3 dangerouslySetInnerHTML={{ __html: product.label }}></h3>
              <p>${product.price}</p>
            </div>
            <Link href={`/products/${product.slug}`} />
          </li>
        ))}
      </ul>
    </main>
  );
};

export default SearchCatalog;
