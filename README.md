# Unit Converter

Simple C->F Converter for INF345 DevOps project.

## what it does
- It sends the resulting calculation of the convert

## how to run it
./scripts/run.sh

## how to test it
./scripts/test.sh

## PORT
Uses $PORT environment variable, defaults to 8080.

## Rollback

Argo CD deploys what is on the `main` branch, from the `k8s` folder.
To roll back, undo the commit that deployed the bad version, with a new commit:

    git log --oneline -- k8s/deployment.yaml
    git revert --no-edit -m 1
    git push

Argo CD deploys the previous version within three minutes. Do not use
`kubectl rollout undo`: self-heal would put the bad version back.
