import ProductCategory from '../../../components/Pages/Home/ProductCategory';
import { ICategory } from '../../utils/interfaces';

async function fetchCategories(): Promise<ICategory[]> {
  const response = await fetch(
    `${process.env.SERVER_URL}/api/v1/categories/parent`
  );
  return response.json();
}

async function CategoriesPage() {
  const categories = await fetchCategories();

  return (
    <main>
      {categories.map((category) => (
        <ProductCategory key={category.id} category={category} />
      ))}
    </main>
  );
}

export default CategoriesPage;
