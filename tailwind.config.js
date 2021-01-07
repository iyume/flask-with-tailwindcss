// do the customization
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
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
