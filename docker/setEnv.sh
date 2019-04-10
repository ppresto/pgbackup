#!/usr/bin/env bash

mypython() {
  docker run -it --rm --name tmp-python \
    -v $HOME:/root \
    -v $HOME/Projects/DevOps/python/dev:/root/bin \
    -e "PATH=${PATH}:/root/bin" \
    ppresto/python3.7 "$@"
}
