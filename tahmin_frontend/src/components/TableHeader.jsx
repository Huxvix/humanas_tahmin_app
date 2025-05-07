import React from 'react';

function TableHeader() {
    const headers = [
      'ID',
      'İsim',
      'Son Giriş',
      'Tahmini Sonraki Giriş (Algoritma 1)',
      'Tahmini Sonraki Giriş (Algoritma 2)',
    ];
    return (
      <thead>
        <tr className="bg-gray-200">
          {headers.map((text, idx) => (
            <th key={idx} className="py-2 px-4">
              {text}
            </th>
          ))}
        </tr>
      </thead>
    )
  }

export default TableHeader;
