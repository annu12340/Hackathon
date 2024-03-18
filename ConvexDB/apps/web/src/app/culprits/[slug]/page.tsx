import Header from '@/components/Header';
import CulpritDetails from '@/components/culprits/CulpritDetails';
import { Id } from '@packages/backend/convex/_generated/dataModel';

export default function Page({ params }: { params: { slug: string } }) {
  return (
    <main className='bg-[#F5F7FE] h-screen'>
      <Header />
      <CulpritDetails culpritId={params.slug as Id<'culprits'>} />
    </main>
  );
}
