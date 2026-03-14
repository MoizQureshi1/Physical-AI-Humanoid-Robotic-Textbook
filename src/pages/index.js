import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import Head from '@docusaurus/Head';

export default function Home() {
  return (
    <Layout>
      <Head>
        <meta http-equiv="refresh" content="0; url=./docs/intro" />
      </Head>
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '50vh',
        fontSize: '1.5rem',
      }}>
        <p>Redirecting to <Link to="/docs/intro">documentation</Link>...</p>
      </div>
    </Layout>
  );
}