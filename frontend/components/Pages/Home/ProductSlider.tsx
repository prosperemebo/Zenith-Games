"use client";
import { useEffect, useState } from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { EffectCoverflow, Autoplay } from "swiper/modules";

import "swiper/css";
import "./style.scss";
import Image from "next/image";
import { IProduct } from "@/utils/interfaces";

const ProductSlider = (): JSX.Element => {
  const [products, setProducts] = useState<IProduct[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        console.log(`${process.env.SERVER_URL}/api/v1/products/recommended`);
        const response = await fetch(
          `${process.env.SERVER_URL}/api/v1/products/recommended`,
        );
        if (!response.ok) {
          throw new Error("Failed to fetch products");
        }
        const data = await response.json();
        setProducts(data);
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
    <Swiper
      loop={true}
      speed={1000}
      autoplay={{
        delay: 3000,
      }}
      effect="coverflow"
      modules={[EffectCoverflow, Autoplay]}
      grabCursor={true}
      centeredSlides={true}
      slidesPerView="auto"
      coverflowEffect={{
        rotate: 0,
        stretch: 100,
        depth: 250,
        modifier: 1.5,
        slideShadows: false,
      }}
    >
      {products.map((product, index) => (
        <SwiperSlide key={product.id}>
          <Image
            width="500"
            height="500"
            draggable="false"
            src={product.cover_image?.split("?")[0]}
            alt={product.label}
            priority={index === 1}
          />
          <h1
            className="heading-primary"
            dangerouslySetInnerHTML={{ __html: product.label }}
          ></h1>
        </SwiperSlide>
      ))}
    </Swiper>
  );
};

export default ProductSlider;
