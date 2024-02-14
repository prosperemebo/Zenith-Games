import { ICategory } from '@/utils/interfaces';
import classes from './Category.module.scss';
import Image from 'next/image';
import Link from 'next/link';

interface Props {
  category: ICategory;
}

const Catalog = ({ category }: Props) => {
  return (
    <main className={classes.wrapper}>
      <h2
        className='heading-primary'
        dangerouslySetInnerHTML={{ __html: category.label }}
      ></h2>
      {category.sub_categories?.length > 0 && (
        <ul className={classes.menu}>
          {category.sub_categories?.map((category) => (
            <li key={category.id}>
              <Link href={`/categories/${category.slug}`} legacyBehavior>
                <a dangerouslySetInnerHTML={{ __html: category.label }}></a>
              </Link>
            </li>
          ))}
        </ul>
      )}
      <p className="paragraph" dangerouslySetInnerHTML={{__html: category.summary}}></p>
      <ul className={classes.products}>
        {category.products.map((product, index) => (
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
          </li>
        ))}
      </ul>
    </main>
  );
};

export default Catalog;
