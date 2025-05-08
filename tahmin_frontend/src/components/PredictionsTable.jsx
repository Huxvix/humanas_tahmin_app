import React from 'react';
import TableHeader from './TableHeader';
import TableBody from './TableBody';
import './PredictionsTable.css';

function PredictionsTable({ data }) {
  return (
    <div className="overflow-x-auto mx-auto">
      <table className="table table-bordered table-sm table-striped table-hover table-fixed">
        <TableHeader />
        <TableBody data={data} />
      </table>
    </div>
  );
}

export default PredictionsTable;