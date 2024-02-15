import { ICategory } from '@/utils/interfaces';
import Catalog from '../../../../components/Pages/Category/Catalog';

async function fetchPageData(slug: string): Promise<ICategory> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/categories/${slug}/products?per_page=200`,
    { next: { revalidate: 10 } }
  );
  return response.json();
}

async function CategoryPage({params}: any) {
  const category = await fetchPageData(params.slug)

  return <Catalog category={category} />;
}

export default CategoryPage;
