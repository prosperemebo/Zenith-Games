export interface ICategory {
  id: string;
  label: string;
  slug: string;
  products: IProduct[],
  sub_categories: ICategory[],
  summary: string
}

export interface IProduct {
  id: string;
  label: string;
  cover_image: string;
  price: number;
}
