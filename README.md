# Step to setup and run

## Environment
```
cd WORKDIR
python3 -m venv venv
source venv/bin/activate # make sure you're in the virtualenv
pip3 install -r requirements.txt -i https://speedup.registry.com/simple # replace source
nvm use node
npm i autoprefixer postcss postcss-cli tailwindcss
```
To use form, you are required to do extra installation

**form plugin installation**
```
npm i @tailwindcss/forms
```

**form plugin includation**

Look `tailwind.config.css` for `plugins` option, add `require('@tailwindcss/forms'),`

## Strip unused css
> Use it if you are in developing

**Turn on the purgecss**

Edit `tailwind.config.js`

Find the key `purge` and set its key `enabled`'s value to `true`

**Then run build**
```
npm run build
```

## Start up
```
flask run
```

## Note

### Functions
`theme()`
> Inner variable selector

- Example
```
theme('height.1')
theme('borderWidth.t.DEFAULT')
theme('borderWidth.t[DEFAULT]') # do the same role
```

**addBase()**
> Extra customization - to do with plugin - little advanced

- Use plugin
```
const plugin = require('tailwindcss/plugin')
```

- Usage - with some tricks
```
plugins: [
  plugin(function({ theme, addBase }) {
    addBase({
      'hr': {
        borderWidth: theme('borderWidth.t.DEFAULT'),
        'margin': '0.5em auto',
        height: theme('height.1'),
        // 'height': '1px', // do the same thing
      },
    })
  }),
  require('@tailwindcss/forms'),
],
```
