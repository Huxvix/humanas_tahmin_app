import React from 'react';
import TableRow from './TableRow';

function TableBody({ data }) {
  if (!data.length) {
    return (
      <tbody>
        <tr>
          <td colSpan={5} className="py-4 text-center text-gray-500">
            Sonuç bulunamadı.
          </td>
        </tr>
      </tbody>
    );
  }

  return (
    <td className='px-1 py-0.5 sm:px-2 sm:py-1'> 
      {data.map(user => (
        <TableRow key={user.user_id} user={user} />
      ))}
    </td>
  );
}

export default TableBody;