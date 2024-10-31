import React, { useState } from 'react';
import axios from 'axios';

function Register() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState(''); // สถานะสำหรับข้อความตอบสนอง

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/register', {
        username: username,
        email: email,
        password: password
      });
      setMessage(response.data.message); // ตั้งค่าข้อความตอบสนอง
    } catch (error) {
      setMessage('Registration failed. Please try again.'); // ข้อความเมื่อเกิดข้อผิดพลาด
    }
  };

  return (
    <div>
      <h1>Register User</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Register</button>
      </form>
      {message && <p>{message}</p>} {/* แสดงข้อความตอบสนอง */}
    </div>
  );
}

export default Register;

// import React, { useState } from 'react';
// import axios from 'axios';

// function Register() {
//   const [username, setUsername] = useState('');
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [message, setMessage] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       const response = await axios.post('http://127.0.0.1:5000/register', {
//         username: username,
//         email: email,
//         password: password,
//       });
//       setMessage(response.data.message); // หากสำเร็จให้แสดงข้อความจาก server
//     } catch (error) {
//       setMessage('Registration failed. Please try again.'); // หากล้มเหลวให้แสดงข้อความผิดพลาด
//       console.error('Error:', error);
//     }
//   };

//   return (
//     <div>
//       <h1>Register User</h1>
//       <form onSubmit={handleSubmit}>
//         <input
//           type="text"
//           placeholder="Username"
//           value={username}
//           onChange={(e) => setUsername(e.target.value)}
//         />
//         <input
//           type="email"
//           placeholder="Email"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//         />
//         <input
//           type="password"
//           placeholder="Password"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//         />
//         <button type="submit">Register</button>
//       </form>
//       <p>{message}</p>
//     </div>
//   );
// }

// export default Register;
