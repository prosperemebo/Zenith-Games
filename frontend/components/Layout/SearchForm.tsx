'use client';

import { useState } from 'react';
import { IoSearch } from 'react-icons/io5';
import classes from './Layout.module.scss';
import { useRouter } from 'next/navigation';

const SearchForm = ({ productCount }: { productCount: number }) => {
  const [searchQuery, setSearchQuery] = useState<string>('');
  const router = useRouter();

  function handleSubmit(e: any): void {
    e.preventDefault();
    router.push(`/search?query=${searchQuery}`);
  }

  return (
    <form className={classes.inputWrapper} onSubmit={handleSubmit}>
      <input
        type='text'
        placeholder={`Search over ${productCount} products...`}
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button type='submit'>
        <span>
          <IoSearch />
        </span>
      </button>
    </form>
  );
};

export default SearchForm;
