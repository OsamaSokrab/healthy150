import React from 'react';
import SearchSpeaker from './components/SearchSpeaker/SearchSpeaker';
import Counter from './components/Counter';
import Dashboard from './components/Dashboard';
import Dashboard4 from './components/Dashboard4';

function App() {
  return (
    <div style={{
      backgroundColor: 'green', margin: 20,
      color: 'white'
    }}>
      <h1>...</h1>
      …..
      <Dashboard />
      <SearchSpeaker />
      <Counter />
      <Dashboard4 />
    </div>
  );
}
export default App;