'use client';
import Header from '@/components/Header';
import axios from 'axios';


import React, { useEffect, useState } from 'react';

const MapViewer = () => {
  const [mapUrl, setMapUrl] = useState('');

  useEffect(() => {
    const fetchMap = async () => {
      try {
        const response = await axios.post('http://127.0.0.1:5000/map', {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
          }
        });
        
        if (response.status === 200) {
          const html_data = response.data;
          console.log("html_data",html_data)
          setMapUrl(html_data);
  
        } else {
          console.error('Failed to fetch map:', response.statusText);
        }
      } catch (error) {
        console.error('Error fetching map:', error);
      }
      window.location.href = 'http://localhost:3000/map';
    };

    fetchMap();
  }, []);

  return (
    <div>
              <Header />
        
    {mapUrl ? (
      <div dangerouslySetInnerHTML={{ __html: mapUrl }} />
    ) : (
      <h3>No data is found</h3>
    )}

    </div>
  );
};

export default MapViewer;

