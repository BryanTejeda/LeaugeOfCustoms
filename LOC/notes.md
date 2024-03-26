Well Notes on Tech used in the application and things to make me better conceputalize concepts

So far we have Flask working as our backend server thing that is handling rendering and logic behind the scences of the site.
We are using the bootstrap css library to make elements and html look good. 
Not Much Javascript atm. 

# Websockets
https://www.reddit.com/r/flask/comments/if7po9/how_my_friend_and_i_built_a_multiplayer_game/
https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent
https://youtu.be/zQDzNNt6xd4

Communication protocol in Html5. It allows servers and clients to communicate with each other bidirectionally. 
Good for use in games or sites where we need to display live information with very low latency

There seems to be a native flask extension called Flask-Sockets, but that is different than Flask-SocketIO.
Flask-SocketIO is a wrapper for the former

SocketIO is a websocket library in Javascript. 
