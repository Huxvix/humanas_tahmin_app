import React from 'react';
import TableHeader from './TableHeader';
import TableBody from './TableBody';
import './PredictionsTable.css';

function PredictionsTable({ data }) {
  return (
    <div className="overflow-x-auto mx-auto w-full px-2 sm:px-4">
      <table
        className="table-fixed w-fulltext-xs sm:text-sm md:text-base table-striped table-hover table-bordered">
        <TableHeader />
        <TableBody data={data} />
      </table>
    </div>
  );
}

export default PredictionsTable;