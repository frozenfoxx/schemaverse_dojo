""" Objects relating to a sparring match """

import docker

class Kumite(object):
    """ A round of the game """

    def __init__(self, players, gameport):
        self.docker_client = docker.from_env()
        self.game_server = ""
        self.game_server_ip = ""
        self.game_server_port = ""
        self.game_port = gameport
        self.players = players

    def load_container(self):
        """ Loads the container """

        # Start server container
        self.game_server = self.docker_client.containers.run('frozenfoxx/schemaverse:latest',
                                                             detach=True,
                                                             auto_remove=True,
                                                             publish_all_ports=True
                                                            )

        # Retrieve exposed port and IP
        self.game_server_ip = self.docker_client.api.inspect_container(self.game_server.id)['NetworkSettings']['IPAddress']
        self.game_server_port = self.docker_client.api.port(self.game_server.id, self.game_port)[0]['HostPort']

        # Check until DB is ready
        ready = False
        while not ready:
            check_output = str(self.game_server.exec_run('/usr/bin/pg_isready'))
            ready = 'accepting connections' in check_output

    def load_players(self):
        """ Loads the players into the container """

        # Iterate over players to add to game server
        for i in self.players:
            player_add = "/src/schemaverse/scripts/add_player.sh " \
                + str(i) \
                + " " \
                + str(self.players[i])

            self.game_server.exec_run(player_add)
            print("[+] Player added: " + str(i))

    def name(self):
        """ Returns the name of the container """

        return self.game_server.name

    def shutdown(self):
        """ Kills the kumite """

        self.unload_container()

    def status(self):
        """ Reports the status of the kumite """

        return self.game_server.status

    def unload_container(self):
        """ Kills the container """

        self.game_server.stop()
