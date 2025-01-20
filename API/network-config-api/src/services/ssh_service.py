class SSHService:
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        import paramiko
        try:
            self.connection = paramiko.SSHClient()
            self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.connection.connect(self.hostname, username=self.username, password=self.password)
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    def execute_command(self, command):
        if self.connection is None:
            raise Exception("SSH connection not established.")
        stdin, stdout, stderr = self.connection.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()

    def close(self):
        if self.connection:
            self.connection.close()

# TODO: Test med nettverksenhet og skjekk funksjonalitet - MIDLERTIDIG KODE FOR TESTING