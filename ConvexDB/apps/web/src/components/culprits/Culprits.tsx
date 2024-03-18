'use client';
import Image from 'next/image';
import CulpritItem from './CulpritItem';
import CreateCulprit from './CreateCulprit';
import { api } from '@packages/backend/convex/_generated/api';
import { useQuery, useMutation } from 'convex/react';
import { useState } from 'react';

const Culprits = () => {
  const [search, setSearch] = useState('');

  const allCulprits = useQuery(api.culprits.getCulprits);
  const deleteCulprit = useMutation(api.culprits.deleteCulprit);

  const finalCulprits = search
    ? allCulprits?.filter(
        (culprit) =>
        
          culprit.content.toLowerCase().includes(search.toLowerCase())
      )
    : allCulprits;

  return (
    <div className='container mx-auto pb-10'>


   <h1 className='text-center text-2xl sm:text-4xl font-semibold text-gray-800 mt-8 mb-10'>
        Your reports
      </h1>
      <div className='px-5 sm:px-0'>
        <div className='flex items-center gap-2 sm:gap-5 bg-white rounded shadow-md h-12 sm:h-14 mb-10 px-3 sm:px-11'>
          <Image
            src={'/images/search.svg'}
            width={23}
            height={22}
            alt='search'
            className='w-5 h-5 sm:w-6 sm:h-6 cursor-pointer'
          />
          <input
            type='text'
            placeholder='Search'
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className='flex-1 text-sm sm:text-lg text-gray-700 font-light leading-none tracking-tighter border-0 focus:ring-0 focus:border-0'
          />
        
        </div>
      </div>

      <div className='divide-y divide-gray-200 border-t border-b border-gray-200'>
        {finalCulprits &&
          finalCulprits.map((culprit, index) => (
            <CulpritItem key={index} culprit={culprit} deleteCulprit={deleteCulprit} />
          ))}
      </div>
      <br /><br />
      <CreateCulprit />
    </div>
  );
};

export default Culprits;
