'use client';
import Image from 'next/image';
import NoteItem from './NoteItem';
import CreateNote from './CreateNote';
import { api } from '@packages/backend/convex/_generated/api';
import { useQuery, useMutation } from 'convex/react';
import { useState } from 'react';

const Notes = () => {
 const [search, setSearch] = useState('');

 const allNotes = useQuery(api.notes.getNotes);
 const deleteNote = useMutation(api.notes.deleteNote);

 const finalNotes = search
    ? allNotes?.filter(
        (note) =>
          note.title.toLowerCase().includes(search.toLowerCase()) ||
          note.content.toLowerCase().includes(search.toLowerCase())
      )
    : allNotes;

 return (
    <div className='container pb-10 mx-auto'>
      <h1 className='text-center text-2xl sm:text-4xl font-semibold text-gray-800 mt-8 mb-10'>
        Your Notes
      </h1>
      <div className='px-5 sm:px-0'>
        <div className='bg-white flex items-center h-12 sm:h-14 rounded shadow-md gap-2 sm:gap-5 mb-10 px-3 sm:px-11'>
          <Image
            src={'/images/search.svg'}
            width={23}
            height={22}
            alt='search'
            className='cursor-pointer sm:w-6 sm:h-6 w-5 h-5'
          />
          <input
            type='text'
            placeholder='Search'
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className='flex-1 text-gray-700 text-sm sm:text-lg font-light leading-none tracking-tighter border-0 focus:ring-0 focus:border-0'
          />
        </div>
      </div>

      <div className='border-t border-b border-gray-200 divide-y divide-gray-200'>
        {finalNotes &&
          finalNotes.map((note, index) => (
            <NoteItem key={index} note={note} deleteNote={deleteNote} />
          ))}
      </div>

      <CreateNote />
    </div>
 );
};

export default Notes;
