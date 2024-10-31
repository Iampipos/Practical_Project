import React from 'react';
import Register from './components/Register';  // นำเข้า Register Component

function App() {
  return (
    <div className="App">
      <h1>Register User</h1>
      <Register />  {/* เรียกใช้ Register Component */}
    </div>
  );
}

export default App;
