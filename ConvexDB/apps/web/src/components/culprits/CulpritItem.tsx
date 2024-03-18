import Link from 'next/link';
import DeleteCulprit from './DeleteCulprit';

export interface CulpritProps {
  culprit: {
    content: string;
    _id: string;
    _creationTime: number;
  };
  deleteCulprit: any;
}

const CulpritItem = ({ culprit, deleteCulprit }: CulpritProps) => {
  return (
    <div className='flex justify-between items-center h-[74px] bg-[#F9FAFB] py-5 px-5 sm:px-11 gap-x-5 sm:gap-x-10'>
      <Link href={`/culprits/${culprit._id}`} className='flex-1'>
        <h1 className='  text-base font-medium text-black'>
        {culprit.content.split('\n').slice(0, 20).join('\n')}
        </h1>
      </Link>
      <p className='hidden md:flex text-[#2D2D2D] text-center  not-italic font-extralight leading-[114.3%] tracking-[-0.5px]'>
        {new Date(Number(culprit._creationTime)).toLocaleDateString()}
      </p>
      <DeleteCulprit deleteAction={() => deleteCulprit({ CulpritId: culprit._id })} />

    </div>
  );
};

export default CulpritItem;
