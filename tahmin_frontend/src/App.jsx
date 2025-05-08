import React, { useState } from 'react';
import useLoginData from './hooks/useLoginData';
import SearchBar from './components/SearchBar';
import PredictionsTable from './components/PredictionsTable';
import 'bootstrap/dist/css/bootstrap.css';

export default function App() {
  const { data, loading, error } = useLoginData();
  const [searchTerm, setSearchTerm] = useState('');

  // Arama terimini kullanarak verileri filtreleme lojiği
  const filteredData = data.filter(user => {
    const term = searchTerm.toLowerCase();
    return (
      user.user_name.toLowerCase().includes(term) ||
      String(user.user_id).includes(term)
    );
  });

  if (loading) return <p className="p-4 text-center">Yükleniyor...</p>;
  if (error)   return <p className="p-4 text-red-500 text-center">Error: {error.message || error}</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4 text-center">Login Tahminleri</h1>

      <SearchBar
        value={searchTerm}
        onChange={e => setSearchTerm(e.target.value)}
      />

      <PredictionsTable data={filteredData} />
    </div>
  );
}
