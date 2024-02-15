import { IProduct } from '@/utils/interfaces';
import classes from './Product.module.scss';
import Image from 'next/image';

async function fetchPageData(slug: string): Promise<IProduct> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/products/${slug}`,
    { next: { revalidate: 10 } }
  );

  return response.json();
}

async function ProductPage({ params }: any) {
  const product = await fetchPageData(params.id);

  return (
    <main className={classes.wrapper}>
      <header className={classes.header}>
        <figure className={classes.composition}>
          <Image
            width='500'
            height='500'
            draggable='false'
            src={product.cover_image?.split('?')[0]}
            alt={product.label}
            priority={true}
          />
        </figure>
        <div className={classes.info}>
          <h1
            className='heading-primary'
            dangerouslySetInnerHTML={{ __html: product.label }}
          ></h1>
          <p className={classes.price}>${product.price}</p>
          <p
            className={classes.summary}
            dangerouslySetInnerHTML={{ __html: product.summary }}
          ></p>
        </div>
      </header>
      <section
        className={classes.body}
        dangerouslySetInnerHTML={{ __html: product.description }}
      ></section>
    </main>
  );
}

export default ProductPage;
