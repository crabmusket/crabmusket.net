# Content and infrastructure of [crabmusket.net](https://crabmusket.net)

## Spinning up a new service

1. Create file `init/thing`
2. `git add init/thing`, commit, and push
3. In the server, `cp init/thing /etc/systemd/system`
4. `systemctl enable thing` and `systemctl start thing`
