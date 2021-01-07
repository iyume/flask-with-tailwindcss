# Step to setup and run

## Environment
```
cd WORKDIR
python3 -m venv venv
source venv/bin/activate # make sure you're in the virtualenv
pip3 install -r requirements.txt -i https://speedup.registry.com/simple # replace with the domestic source
nvm use node
npm i autoprefixer postcss postcss-cli tailwindcss
```

## Strip unused css
> Use it if you are in developing

- Turn on the purgecss
Switch to `tailwind.config.js`
Find the key `purge` and set its key `enabled`'s value to `true`

- Then
```
npm run build
```

## Start up
```
flask run
```
