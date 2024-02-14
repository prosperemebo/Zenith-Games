/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    domains: ['i0.wp.com'],
  },
  env: {
    SERVER_URL: process.env.SERVER_URL,
  },
  webpack(config) {
    config.module.rules.push({
      test: /\.svg$/,
      use: [
        {
          loader: '@svgr/webpack',
          options: {
            svgoConfig: {
              plugins: [
                {
                  name: 'removeViewBox',
                  active: false,
                },
              ],
            },
          },
        },
      ],
    });

    return config;
  },
};

export default nextConfig;
