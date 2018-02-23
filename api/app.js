const koa = require('koa'); // koa@2
const koaRouter = require('koa-router'); // koa-router@next
const koaBody = require('koa-bodyparser'); // koa-bodyparser@next
const { graphqlKoa, graphiqlKoa } = require('apollo-server-koa');
const { schema } = require('./src/schema');

const app = new koa();
const router = new koaRouter();
const PORT = 8080;

// koaBody is needed just for POST.
router.post('/graphql', koaBody(), graphqlKoa({ schema }));
router.get('/graphql', graphqlKoa({ schema }));
router.get('/graphiql', graphiqlKoa({ endpointURL: '/graphql' }),);

app.use(router.routes());
app.use(router.allowedMethods());
app.listen(PORT);
