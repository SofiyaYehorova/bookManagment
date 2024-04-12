import React, {useEffect, useState} from 'react';
import axios from "axios";

const App = () => {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    axios.get('/api/books').then(({data})=>setBooks(data.results))
  }, []);

    return (
        <div>
          <h1>Books: </h1>
          {books.map(book=><div key={book.id}>{book.name} {book.author}</div>)}
        </div>
    );
};

export {App};