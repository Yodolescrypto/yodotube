# yodotube
Yodotoube

## Install

You will need to install [go-ipfs](https://github.com/ipfs/go-ipfs) first.

### System Requirements

You will need to install python3 and pip:

```bash
$> sudo apt update
$> sudo apt install python3 python3-venv
```

### Python part

Clone the project:

```bash
$> git clone git@github.com:Yodolescrypto/yodotube.git
```

Start a new virtualenv then install pip dependencies:

```bash
$> cd yodotube/yodotube
$> virtualenv $PWD/venv
$(venv)> source $PWD/venv/bin/activate
$(venv)> pip3 install -r requirements.txt
```

Make the migrations and create your superuser (the first time only):

```bash
$(venv)> python3 manage.py migrate
$(venv)> python3 manage.py createsuperuser
```

### Starting to run everything

Last step: Start IPFS node in daemon mode:

```bash
$> ipfs daemon&
```

You may use `screen`:

```bash
$> screen -dmS ipfs ipfs daemon
$> screen -r ipfs #to get it back, then ctrl-a, d to detach it again
```

Then start your django project:

```bash
$> screen -dmS yodotube $PWD/venv/bin/python3 manage.py runserver
$> screen -r yodotube #to get it back, then ctrl-a, d to detach it again
```

## Use it

Go on [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Admin Panel

You may find the admin panel here: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
