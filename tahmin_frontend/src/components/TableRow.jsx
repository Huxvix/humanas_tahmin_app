import React from 'react';

function TableRow({ user }) {
  return (
    <tr className="border-t hover:bg-gray-50">
      <td className="py-2 px-4 text-center">{user.user_id}</td>
      <td className="py-2 px-4 text-center">{user.user_name}</td>
      <td className="py-2 px-4 text-center">{user.last_login}</td>
      <td className="py-2 px-4 text-center">{user.predicted_next_mean}</td>
      <td className="py-2 px-4 text-center">{user.predicted_next_median}</td>
    </tr>
  );
}

export default TableRow;