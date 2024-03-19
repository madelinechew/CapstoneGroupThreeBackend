module.exports = ({ env }) => ({
  auth: {
    secret: 'uPJn/FeTbf+z3nMzwJrAIQ==',
  },
  apiToken: {
    salt: '7Cy3w2t5bKEj+J4AmMfwWg==',
  },
  transfer: {
    token: {
      salt: env('TRANSFER_TOKEN_SALT'),
    },
  },
  flags: {
    nps: env.bool('FLAG_NPS', true),
    promoteEE: env.bool('FLAG_PROMOTE_EE', true),
  },
});
