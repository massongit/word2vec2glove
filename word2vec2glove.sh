#!/usr/bin/env bash -eu
# Convert Word2Vec model to GloVe format

tail -n +2 ${1} > ${2}
