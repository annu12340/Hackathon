'use client';

import { Disclosure } from '@headlessui/react';
import { Bars3Icon, XMarkIcon } from '@heroicons/react/24/outline';

import Logo from './common/Logo';
import Link from 'next/link';
import { useUser } from '@clerk/clerk-react';
import { UserNav } from './common/UserNav';
import { usePathname } from 'next/navigation';


export default function Header() {
  const { user } = useUser();
  const pathname = usePathname();
 
 
  const navigation = [
     { name: 'Home', href: '/', current: pathname === '/' },
     { name: 'Encode', href: '/encode', current: pathname === '/encode' },
     { name: 'Report', href: '/culprits', current: pathname === '/culprits' },

  ];
 
  return (
     <Disclosure as='nav' className='bg-white shadow'>
       {({ open }) => (
         <>
           <div className='container mx-auto px-2 sm:px-0'>
             <div className='flex items-center justify-between h-16 sm:h-20'>
               <div className='flex items-center'>
                Sentinel <Logo isMobile={true} />
               </div>
               <div className='hidden sm:block'>
                 <div className='ml-10 flex items-baseline space-x-4'>
                  {navigation.map((item) => (
                     <Link
                       key={item.name}
                       href={item.href}
                       className='text-sm font-medium hover:text-gray-900'
                       aria-current={item.current ? 'page' : undefined}
                     >
                       {item.name}
                     </Link>
                   ))}
                 </div>
               </div>
               <div className='sm:hidden'>
               <Disclosure.Button className='relative inline-flex  items-center justify-center rounded-md p-2 text-gray-400 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white'>
                    <span className='absolute -inset-0.5' />
                    <span className='sr-only'>Open main menu</span>
                    {open ? (
                      <XMarkIcon className='block h-6 w-6' aria-hidden='true' />
                    ) : (
                      <Bars3Icon className='block h-6 w-6' aria-hidden='true' />
                    )}
                  </Disclosure.Button>
               </div>
               {user ? (
                 <div className='hidden sm:block sm:ml-6'>
                  <UserNav
                     image={user?.imageUrl}
                     name={user?.fullName!}
                     email={user?.primaryEmailAddress?.emailAddress!}
                  />
                 </div>
               ) : (
                 <div className='hidden sm:block sm:ml-6'>
                  <Link
                     href='/notes'
                     className='text-white bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-md font-medium'
                  >
                     Sign in
                  </Link>
                  <Link
                     href='/notes'
                     className='ml-4 text-sm text-blue-700 hover:text-blue-800'
                  >
                     Get Started
                  </Link>
                 </div>
               )}
             </div>
           </div>
         </>
       )}
     </Disclosure>
  );
 }
 