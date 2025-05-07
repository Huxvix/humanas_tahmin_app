import React from 'react';

function TableRow({ user }) {
  return (
    <tr className="border-t hover:bg-gray-50">
      <td className="py-2 px-4 text-center">{user.user_id}</td>
      <td className="py-2 px-4">{user.user_name}</td>
      <td className="py-2 px-4">{user.last_login}</td>
      <td className="py-2 px-4">{user.predicted_next_mean}</td>
      <td className="py-2 px-4">{user.predicted_next_exsm}</td>
    </tr>
  );
}

export default TableRow;