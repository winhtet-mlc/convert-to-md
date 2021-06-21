#!/bin/bash -eux



GIT_REPO="git@github.com:${CIRCLE_PROJECT_USERNAME}/${CIRCLE_PROJECT_REPONAME}.git"



git submodule init
git submodule update



remote=`git ls-remote --heads 2> /dev/null | grep deploy || true`



if [ -n "$remote" ]; then
  git clone -b deploy "${GIT_REPO}" public
  rm -rf public/*
else
  git init public
  cd public
  git checkout -b deploy
  git remote add origin "${GIT_REPO}"
  cd ..
fi



git config --global user.email "${GIT_USER_EMAIL}"
git config --global user.name "${GIT_USER_NAME}"
git clone "${GIT_REPO}"
ls
hugo
cd public
pwd
git add -A
git commit -m "Automated deploy process from master branch"
git push -f origin deploy
git checkout deploy
pythpn -m http.server 8000
