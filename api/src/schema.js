const { makeExecutableSchema } = require('graphql-tools');

// Some fake data
const books = [
  {
    title: "Harry Potter and the Sorcerer's stone",
    author: 'J.K. Rowling',
  },
  {
    title: 'Jurassic Park',
    author: 'Michael Crichton',
  },
];

// The GraphQL schema in string form
const typeDefs = `
  type Query {
    book(title: String): Book
    allBooks: [Book]
  }
  type Book { title: String, author: String }
`;

// The resolvers
const resolvers = {
  Query: {
    allBooks: () => books,
    book: (root, args) => {
      console.log(root, args);
      return books.find(b => b.title === args.title);
    }
  },
};

// Put together a schema
const schema = makeExecutableSchema({
  typeDefs,
  resolvers,
});

exports.schema = schema;
