'use client';

import { api } from '@packages/backend/convex/_generated/api';
import { Id } from '@packages/backend/convex/_generated/dataModel';
import { useQuery } from 'convex/react';
import Link from 'next/link';
import { useState } from 'react';


interface CulpritDetailsProps {
  culpritId: Id<'culprits'>;
}

const CulpritDetails = ({ culpritId }: CulpritDetailsProps) => {
  const [isSummary, setIsSummary] = useState(false);
  const currentCulprit = useQuery(api.culprits.getCulprit, { id: culpritId });
  const [similarReport, setSimilarReport] = useState<any>(null);

  const handleViewSimilarReport = async () => {

    try {
      const response = await fetch('http://localhost:8080/similar');
      const json_data = await response.json();
      const data = { 'similarity': json_data }
      setSimilarReport(data);
      console.log(data);
    } catch (error) {
      console.error('Error fetching similar reports:', error);
    }
  };

  return (
    <div className='container space-y-6 sm:space-y-9 py-20 px-[26px] sm:px-0'>
      <h3 className='text-black text-center pb-5 text-xl sm:text-[32px] not-italic font-semibold leading-[90.3%] tracking-[-0.8px]'>
        Detailed description
      </h3>
      <p>{currentCulprit?.content}</p>
      {!similarReport && (
        <button
          type='button'
          className='main-btn mt-4'
          onClick={handleViewSimilarReport}
        >
          View similar report
        </button>
      )}


      <Link
        href='/map'>
        <button
          type='button'
          className='main-btn ml-4'>Track culprit path
        </button>
      </Link>

      {similarReport && (
        <div className='mt-8'>
          <h3 className='text-xl font-semibold mb-4'>Similar Reports</h3>
          <table className='table-auto border-collapse border border-gray-400'>
            <thead>
              <tr>
                <th className='border border-gray-400 px-4 py-2'>Content</th>
              </tr>
            </thead>
            <tbody>
              {similarReport.similarity.map((report) => (
                <tr >
                  <td className='ml-20 border border-gray-400 px-4 py-2'><span>{report}  </span>            <span> <button
                    type='button'
                    className='bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline'
                    onClick={handleViewSimilarReport}
                  >
                    View reported user details
                  </button></span></td>

                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default CulpritDetails;
