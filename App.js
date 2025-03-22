import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [animalData, setAnimalData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAnimal = async () => {
      try {
        const response = await axios.get(
          'https://api.jsongpt.com/json?prompt=Tell me about the Cheetah &taxonomy=array &locations=array &characteristics=array'
        );
        setAnimalData(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchAnimal();
  }, []);

  if (loading) return <p>Loading...</p>;

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial' }}>
      <h1>{animalData.name}</h1>
      <h2>Taxonomy:</h2>
      <ul>
        {animalData.taxonomy.map((tax, index) => (
          <li key={index}>{tax}</li>
        ))}
      </ul>
      <h2>Locations:</h2>
      <ul>
        {animalData.locations.map((loc, index) => (
          <li key={index}>{loc}</li>
        ))}
      </ul>
      <h2>Characteristics:</h2>
      <ul>
        {animalData.characteristics.map((char, index) => (
          <li key={index}>{char}</li>
        ))}
      </ul>
    </div>
  );
};

export default App;
