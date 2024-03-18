'use client';

import { Fragment, useRef, useState } from 'react';
import { Dialog, Transition } from '@headlessui/react';
import axios from 'axios';


export default function Encode() {
  const [open, setOpen] = useState(true);
  const [content, setContent] = useState('');
  
  const cancelButtonRef = useRef(null);
  const encodedMessage = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/encode', { text: content }, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json'
        }
      });
      console.log(response.data); // Log the response data
    } catch (error) {
      console.error(error);
    }
 };

  const createEncodedMessageHandler = async () => {

     console.log("content is ",content)
     await encodedMessage();
     setOpen(false);
  };
 
  return (


<Transition.Root show={open} as={Fragment}>
 <Dialog
    as='div'
    className='relative z-10'
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

    <form className='fixed inset-0 z-10 w-screen overflow-y-auto'>
      <div className='flex min-h-full items-end justify-center p-2 text-center sm:items-center sm:p-0'>
        <Transition.Child
          as={Fragment}
          enter='ease-out duration-300'
          enterFrom='opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95'
          enterTo='opacity-100 translate-y-0 sm:scale-100'
          leave='ease-in duration-200'
          leaveFrom='opacity-100 translate-y-0 sm:scale-100'
          leaveTo='opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95'
        >
          <Dialog.Panel className='relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg p-6 pb-4'>
            <div className='bg-white px-4 pb-4 pt-5 sm:p-8 sm:pb-4'>
              <>
                <div className='mt-3 sm:mt-0 text-left'>
                 <div className='mt-2 space-y-3'>
                    <div className=''>
               
                      <label
                        htmlFor='description'
                        className='block text-base font-medium text-black'
                      >
                           Enter the text you want to encode
                      </label>
                      <div className='mt-2 pb-[18px]'>
                        <textarea
                          id='description'
                          name='description'
                          rows={8}
                          placeholder=''
                          className='block w-full rounded-md border-0 py-1.5 border-[#D0D5DD] shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 ring-2 ring-rose-500/50 sm:leading-6 text-black text-[17px] not-italic font-light leading-[90.3%] tracking-[-0.425px] '
                          value={content}
                          onChange={(e) => setContent(e.target.value)}
                        />
                      </div>
                    </div>
                 </div>
                </div>
              </>
            </div>
            <div className='px-4 py-3 mb-5 flex justify-center items-center'>
              <button
                type='button'
                className='main-btn'
                onClick={createEncodedMessageHandler}
              >
                Create
              </button>
            </div>
          </Dialog.Panel>
        </Transition.Child>
      </div>
    </form>
 </Dialog>
</Transition.Root>

  
  );
 }
 