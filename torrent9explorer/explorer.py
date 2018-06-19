from torrent9explorer.terminal import Terminal


class Explorer:

    def initialize(self):
        self.terminal = Terminal()
        self.terminal.cmdloop()
