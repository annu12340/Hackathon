'use client';
import { Fragment, useRef, useState } from 'react';
import { Dialog, Transition } from '@headlessui/react';
import Image from 'next/image';
import { api } from '@packages/backend/convex/_generated/api';
import { useMutation } from 'convex/react';

export default function CreateCulprit() {
  const [open, setOpen] = useState(false);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [isChecked, setIsChecked] = useState(false);
  const [eyeColor, setEyeColor] = useState('');
  const [hair, setHair] = useState('');
  const [age, setAge] = useState('');
  const [description, setDescription] = useState('');

  const cancelButtonRef = useRef(null);

  const createCulprit = useMutation(api.culprits.createCulprit);

  const createUserCulprit = async () => {
    let content = getCulpritSummary()
    await createCulprit({
      title,
      content,
      isSummary: isChecked,
    });
    setOpen(false);
  };

  const getCulpritSummary = () => {
    let summary = 'Culprit ';

    if (eyeColor) summary += `has ${eyeColor} eyes. `;
    if (hair) summary += `He has ${hair} hair. `;
    if (age) summary += `He is ${age} years old. `;
    if (description) summary += `${description}`;

    return summary.trim();
  };

  return (
    <>
      <div className='flex justify-center items-center'>
      
      <button onClick={() => setOpen(true)}
                type='button'
                className='main-btn'
               
              >          <Image
              src={'/images/Add.png'}
              width={40}
              height={40}
              alt='search'
              className='float-right sm:w-[40px] sm:h-[40px] w-6 h-6'
            />
               
                <span className=''>
            {' '}
            Add new report
          </span>
              </button>
   
      </div>

      <Transition.Root show={open} as={Fragment}>
        <Dialog
          as='div'
          className='fixed inset-0 z-10 overflow-y-auto'
          initialFocus={cancelButtonRef}
          onClose={setOpen}
        >
          <Transition.Child
            as={Fragment}
            enter='ease-out duration-300'
            enterFrom='opacity-0'
            enterTo='opacity-100'
            leave='ease-in duration-200'
            leaveFrom='opacity-100'
            leaveTo='opacity-0'
          >
            <div className='fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity' />
          </Transition.Child>

          <Transition.Child
            as={Fragment}
            enter='ease-out duration-300'
            enterFrom='opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95'
            enterTo='opacity-100 translate-y-0 sm:scale-100'
            leave='ease-in duration-200'
            leaveFrom='opacity-100 translate-y-0 sm:scale-100'
            leaveTo='opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95'
          >
            <Dialog.Panel className='fixed inset-0 flex items-center justify-center'>
              <div className='relative max-w-lg mx-auto p-4'>
                <div className='bg-white rounded-lg shadow-lg'>
                  <div className='p-4'>
                    <h3 className='text-xl font-medium mb-4'>Report new crime</h3>
        
                    <input
                      type='text'
                      id='eyeColor'
                      name='eyeColor'
                      placeholder='Eye Color'
                      className='w-full p-3 text-lg rounded-md border border-gray-300 shadow-sm placeholder-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:outline-none mb-4'
                      value={eyeColor}
                      onChange={(e) => setEyeColor(e.target.value)}
                    />
                    <input
                      type='text'
                      id='hair'
                      name='hair'
                      placeholder='Hair'
                      className='w-full p-3 text-lg rounded-md border border-gray-300 shadow-sm placeholder-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:outline-none mb-4'
                      value={hair}
                      onChange={(e) => setHair(e.target.value)}
                    />
                    <input
                      type='text'
                      id='age'
                      name='age'
                      placeholder='Age'
                      className='w-full p-3 text-lg rounded-md border border-gray-300 shadow-sm placeholder-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:outline-none mb-4'
                      value={age}
                      onChange={(e) => setAge(e.target.value)}
                    />
                   <textarea
                      id='description'
                      name='description'
                      rows={8}
                      placeholder='Other description'
                      className='w-full p-3 text-lg rounded-md border border-gray-300 shadow-sm placeholder-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 focus:outline-none mb-4'
                      value={description}
                      onChange={(e) => setDescription(e.target.value)}
                    />
                    <button
                      type='button'
                      className='main-btn'
                      onClick={createUserCulprit}
                    >
                      Add
                    </button>
                  </div>
                </div>
              </div>
            </Dialog.Panel>
          </Transition.Child>
        </Dialog>
      </Transition.Root>
    </>
  );
}
