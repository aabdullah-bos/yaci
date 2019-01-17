**Warning**:

This Dockerfile is intended for the development of `yaci`, attempting to use it to develop your application may require hacking the Dockerfile.

This directory contains a Dockerfile that can be used for the development of `yaci`. If you'd like to use `yaci` to develop your application, and you perform your development in docker it is advised that you install `yaci` in your applications docker image. If you need to hack `yaci` in your development image, then you should clone the `yaci` repository and mount the cloned repository in your docker container.

## Usage

To use this Dockerfile run the command:

```
docker build -t yaci .
```

This will build a Python 3.7 alpine image. To start developing run the command:

```
docker run --rm -ti -v [PATH_TO_YOUR_LOCAL_YACI_REPO]:/yaci yaci:latest
```

## Known limitations

Other than what I've stated you'll need to cleanup the Python Bytecode in the tests directory. *Investigating why this is happening*
