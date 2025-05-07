import React from 'react';
import TableHeader from './TableHeader';
import TableBody from './TableBody';

function PredictionsTable({ data }) {
  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white rounded-lg shadow-md">
        <TableHeader />
        <TableBody data={data} />
      </table>
    </div>
  );
}

export default PredictionsTable;