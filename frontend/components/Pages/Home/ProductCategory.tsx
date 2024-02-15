"use client";
import { ICategory, IProduct } from "@/utils/interfaces";
import classes from "./ProductCategory.module.scss";
import { useEffect, useState } from "react";
import Image from "next/image";
import Link from "next/link";

interface Props {
  category: ICategory;
}

const ProductCategory = ({ category }: Props) => {
  const [products, setProducts] = useState<IProduct[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch(
          `${process.env.SERVER_URL}/api/v1/categories/${category.id}/products?per_page=10`,
          { cache: "no-store" },
        );

        if (!response.ok) {
          throw new Error("Failed to fetch products");
        }

        const data = await response.json();

        setProducts(data.products);
        setIsLoading(false);
      } catch (error: any) {
        setError(error.message);
        setIsLoading(false);
      }
    };

    fetchProducts();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className={classes.wrapper}>
      <div className={classes.headWrapper}>
        <h2
          className="heading-primary"
          dangerouslySetInnerHTML={{ __html: category.label }}
        ></h2>
        <Link href={`/categories/${category.slug}`} legacyBehavior>
          <a className="btn btn-primary">
            <span>View All</span>
          </a>
        </Link>
      </div>
      <ul className={classes.products}>
        {products.map((product, index) => (
          <li key={product.id}>
            <Image
              width="500"
              height="500"
              draggable="false"
              src={product.cover_image?.split("?")[0]}
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
    </div>
  );
};

export default ProductCategory;
