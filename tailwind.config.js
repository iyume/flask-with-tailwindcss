// do the customization
const colors = require('tailwindcss/colors')

module.exports = {
  purge: {
    enabled: false, // set to false if you are in developing
    preserveHtmlElements: true,
    content: [
    './templates/*.html',
    ],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      white: '#ffffff',
      gray: colors.trueGray,
      yellow: colors.amber,
      blue: colors.lightBlue,
      red: colors.rose,
      pink: colors.fuchsia,
    },
    extend: {
      width: {
        'normal': '1160px',
      },
      colors: {
        'darkless': '#f8f8f8',
        'darker': '#e9ebec',
        'darkest': '#000000',
        },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
