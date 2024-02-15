import { IProduct } from '@/utils/interfaces';
import React from 'react';
import SearchCatalog from '../../../../components/Pages/Search/SearchCatalog';

async function fetchPageData(query: string): Promise<IProduct[]> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/products/search?query=${query}`,
    { next: { revalidate: 10 } }
  );
  return response.json();
}

async function SearchPage({ searchParams }: any) {
  const products = await fetchPageData(searchParams.query);

  return <SearchCatalog products={products} />;
}

export default SearchPage;
