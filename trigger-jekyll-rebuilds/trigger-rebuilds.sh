#!/usr/bin/env bash

set -e

for repo in hsf-training/hsf-training-matplotlib hsf-training/hsf-training-scikit-hep-webpage-minimal hsf-training/hsf-training-scikit-hep-webpage hsf-training/hsf-training-cmake-webpage hsf-training/hsf-training-cicd-github hsf-training/hsf-training-advanced-git-webpage hsf-training/hsf-training-cms-analysis-webpage hsf-training/hsf-training-cicd hsf-training/hsf-training-ml-webpage hsf-training/hsf-training-cicd-basics-webpage hsf-training/hsf-training-ssh-webpage hsf-training/hsf-training-uproot-webpage hsf-training/hsf-training-docker hsf-training/hsf-training-spack-webpage hsf-training/hsf-training-cpp-webpage; do
    echo $repo
    curl -u klieret:$(cat ~/gh_token.txt) -X POST https://api.github.com/repos/$repo/pages/builds
done
