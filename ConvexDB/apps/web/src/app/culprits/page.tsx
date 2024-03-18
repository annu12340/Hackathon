import Header from '@/components/Header';
import Culprits from '@/components/culprits/Culprits';

export default function Home() {
  return (
    <main className='bg-[#EDEDED] h-screen'>
      <Header />
      <Culprits/>
    </main>
  );
}
