import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'

// Create the apollo client
export default function createApolloClient ({ base, endpoints }) {
  let link

  let httpLink = new HttpLink({
    // You should use an absolute URL here
    uri: base + endpoints.graphql,
  })
  // HTTP Auth header injection

  // Apollo cache
  const cache = new InMemoryCache()

  link = httpLink

  const apolloClient = new ApolloClient({
    link,
    cache,
    // Additional options
    ...{
      // This will temporary disable query force-fetching
      ssrForceFetchDelay: 100,
      // Apollo devtools
      connectToDevTools: process.env.NODE_ENV !== 'production',
    },
  })

  return apolloClient
}
