import { ICategory } from '@/utils/interfaces';
import ProductSlider from '../../../components/Pages/Home/ProductSlider';
import ProductCategory from '../../../components/Pages/Home/ProductCategory';

async function fetchCategories(): Promise<ICategory[]> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/categories/parent`,
    { cache: 'no-store' }
  );
  return response.json();
}

async function Home() {
  const categories = await fetchCategories();

  return (
    <main>
      <ProductSlider />
      {categories.map((category) => (
        <ProductCategory key={category.id} category={category} />
      ))}
    </main>
  );
}

export default Home;
