# All the debugging processes

1. In the terminal it could say:

Address already in use
Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port.
On macOS, try disabling the 'AirPlay Receiver' service from System Preferences -> Sharing.

If that's the case, do this in another terminal:
`lsof -i :5000`
`kill <PID>` or `kill -9 <PID>`

And if it doesn't work, you can also run Flask on a different port.
`flask run --port=5001`

2. If you need to terminate the process, use `CTRL+C`.

